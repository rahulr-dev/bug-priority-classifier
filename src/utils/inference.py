import datetime
import os
import time
import pandas as pd
import numpy as np
import re
import scipy.sparse as sp
import joblib
import shap
from sentence_transformers import SentenceTransformer

from src.models.BugData import BugData
from src.models.Prediction import Prediction

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ARTIFACT_DIR = os.path.join(PROJECT_ROOT, "artifacts")

THRESHOLD = 0.10

# ── Priority Heuristic Engine ───────────────────────────────────────────────
CRITICAL_KEYWORDS = [
    "crash", "corrupt", "vulnerability", "security", "deadlock", 
    "nullpointerexception", "npe", "panic", "critical", "severe",
    "failure", "broken", "startup", "data loss", "leak",
    "freeze", "hang", "blocker", "regression", "slowdown"
]

def calculate_heuristic_boost(title: str, description: str) -> float:
    """Calculates a probability boost based on critical keywords."""
    text = (str(title) + " " + str(description)).lower()
    score = 0.0
    for kw in CRITICAL_KEYWORDS:
        if kw in text:
            score += 0.20
    return min(score, 0.7)

# ── Cached singletons ─────────────────────────────────────────────────────────
_ohe = None
_scaler = None
_embedding_model = None
_model = None
_explainer = None


def load_artifacts():
    global _ohe, _scaler, _embedding_model
    if _ohe is None:
        _ohe = joblib.load(os.path.join(ARTIFACT_DIR, "ohe.pkl"))
        _scaler = joblib.load(os.path.join(ARTIFACT_DIR, "scaler.pkl"))
        
        # Load from local directory for offline demo
        local_model_path = os.path.join(ARTIFACT_DIR, "sota_embedding_model")
        
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        _embedding_model = SentenceTransformer(local_model_path, device=device)
        print(f"Loaded all artifacts (SOTA mpnet from LOCAL on {device})..")
    return _ohe, _scaler, _embedding_model


def load_local_model():
    global _model, _explainer
    if _model is None:
        _model = joblib.load(os.path.join(ARTIFACT_DIR, "final_xgboost_path_b.pkl"))
        # Initialize SHAP explainer
        _explainer = shap.TreeExplainer(_model)
        print("Loaded model and SHAP explainer..")
    return _model, _explainer


def clean_text(text: str) -> str:
    text = str(text)
    text = re.sub(r"\([A-Za-z0-9]+\)", "", text)
    text = re.sub(r"\(\d{1,2}/\d{1,2}/\d{1,2}.*?\)", "", text)
    text = re.sub(r"\b[A-Z]{2,3}\s*:", "", text)
    text = text.lower()
    text = re.sub(r"\\t", " ", text)
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def get_feature_names():
    """Helper to get feature names for SHAP visualization."""
    ohe, scaler, _ = load_artifacts()
    
    # Embedding features (768 for mpnet)
    embed_cols = [f"embed_{i}" for i in range(768)]
    
    # Meta features
    meta_cols = list(ohe.get_feature_names_out())
    
    # Additional features
    add_cols = [
        "created_hour", "created_dayofweek", "created_month", "created_year",
        "text_length", "word_count", "avg_word_length"
    ]
    
    return embed_cols + meta_cols + add_cols


def build_features(bug: BugData):
    ohe, scaler, embedding_model = load_artifacts()

    text = clean_text(bug.title + " " + bug.description)
    embeddings = embedding_model.encode([text])
    embeddings_csr = sp.csr_matrix(embeddings)

    meta = pd.DataFrame([{"component": bug.component, "version": bug.version}])
    meta_enc = sp.csr_matrix(ohe.transform(meta))

    dt = datetime.datetime.now()
    if bug.created_time:
        try:
            dt = datetime.datetime.fromisoformat(bug.created_time)
        except:
            pass

    additional_df = pd.DataFrame(
        [
            {
                "created_hour": dt.hour,
                "created_dayofweek": dt.weekday(),
                "created_month": dt.month,
                "created_year": dt.year,
                "text_length": len(text),
                "word_count": len(text.split()),
                "avg_word_length": np.mean([len(w) for w in text.split()]) if text.split() else 0.0,
            }
        ]
    )
    additional_scaled = sp.csr_matrix(scaler.transform(additional_df))

    return sp.hstack([embeddings_csr, meta_enc, additional_scaled])


def build_features_batch(bugs: list[BugData]):
    ohe, scaler, embedding_model = load_artifacts()

    texts = [clean_text(b.title + " " + b.description) for b in bugs]
    embeddings = embedding_model.encode(texts, batch_size=64, show_progress_bar=False)
    embeddings_csr = sp.csr_matrix(embeddings)

    metas = pd.DataFrame([{"component": b.component, "version": b.version} for b in bugs])
    meta_enc = sp.csr_matrix(ohe.transform(metas))

    rows = []
    for b, text in zip(bugs, texts):
        dt = datetime.datetime.now()
        if b.created_time:
            try:
                dt = datetime.datetime.fromisoformat(b.created_time)
            except:
                pass
        words = text.split()
        rows.append(
            {
                "created_hour": dt.hour,
                "created_dayofweek": dt.weekday(),
                "created_month": dt.month,
                "created_year": dt.year,
                "text_length": len(text),
                "word_count": len(words),
                "avg_word_length": np.mean([len(w) for w in words]) if words else 0.0,
            }
        )
    additional_scaled = sp.csr_matrix(scaler.transform(pd.DataFrame(rows)))

    return sp.hstack([embeddings_csr, meta_enc, additional_scaled])


def predict(bug: BugData) -> tuple[Prediction, float, dict]:
    start = time.perf_counter()

    x = build_features(bug)
    model, explainer = load_local_model()
    
    base_prob = float(model.predict_proba(x)[0, 1])
    boost = calculate_heuristic_boost(bug.title, bug.description)
    probability = min(base_prob + boost, 1.0)
    
    prediction = 0 if probability < THRESHOLD else 1
    label = "Low Priority" if prediction == 0 else "High Priority"

    # SHAP Explanation
    shap_values = explainer.shap_values(x)
    
    # We'll return the shap values and feature names for the UI to plot
    explanation = {
        "shap_values": shap_values[0], # For class 1 if multi-class, but XGB binary usually returns one array or list
        "feature_names": get_feature_names(),
        "base_value": explainer.expected_value,
        "input_features": x.toarray()[0]
    }

    elapsed_ms = round((time.perf_counter() - start) * 1000, 2)
    return Prediction(
        label=label, prediction=prediction, probability=round(probability, 4), threshold=THRESHOLD
    ), elapsed_ms, explanation


def predict_batch(bugs: list[BugData]) -> tuple[list[Prediction], float]:
    start = time.perf_counter()

    x = build_features_batch(bugs)
    model, _ = load_local_model()
    base_probs = model.predict_proba(x)[:, 1]

    results = []
    for i, prob in enumerate(base_probs):
        boost = calculate_heuristic_boost(bugs[i].title, bugs[i].description)
        probability = min(float(prob) + boost, 1.0)
        
        prediction = 0 if probability < THRESHOLD else 1
        label = "Low Priority" if prediction == 0 else "High Priority"
        results.append(
            Prediction(
                label=label,
                prediction=prediction,
                probability=round(probability, 4),
                threshold=THRESHOLD,
            )
        )

    elapsed_ms = round((time.perf_counter() - start) * 1000, 2)
    return results, elapsed_ms
