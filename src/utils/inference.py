import datetime
import os
import time
import mlflow
import pandas as pd
import numpy as np
import re
import scipy.sparse as sp
import joblib
from sentence_transformers import SentenceTransformer

from src.models.BugData import BugData
from src.models.Prediction import Prediction

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ARTIFACT_DIR = os.path.join(PROJECT_ROOT, "artifacts")

THRESHOLD = 0.5

# ── Cached singletons ─────────────────────────────────────────────────────────
_ohe = None
_scaler = None
_embedding_model = None
_model = None


def load_artifacts():
    global _ohe, _scaler, _embedding_model
    if _ohe is None:
        _ohe = joblib.load(os.path.join(ARTIFACT_DIR, "ohe.pkl"))
        _scaler = joblib.load(os.path.join(ARTIFACT_DIR, "scaler.pkl"))
        _embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Loaded all artifacts..")
    return _ohe, _scaler, _embedding_model


def load_model():
    global _model
    if _model is None:
        mlflow.set_tracking_uri(
            "sqlite:///D:/Projects/Machine Learning/bug-priority-classifier/mlflow.db"
        )
        _model = mlflow.xgboost.load_model("models:/XGBoostModel@champion")
        print("Loaded model..")
    return _model


def clean_text(text: str) -> str:
    text = str(text)
    # Remove bug IDs like (1GE6IRL)
    text = re.sub(r"\([A-Za-z0-9]+\)", "", text)
    # Remove timestamps like (05/27/01 5:10:19 PM)
    text = re.sub(r"\(\d{1,2}/\d{1,2}/\d{1,2}.*?\)", "", text)
    # Remove name prefixes like "KM:" "EG:"
    text = re.sub(r"\b[A-Z]{2,3}\s*:", "", text)
    # Lowercase
    text = text.lower()
    # Remove tab characters
    text = re.sub(r"\\t", " ", text)
    # Remove special characters
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text


def build_features(bug: BugData):
    ohe, scaler, embedding_model = load_artifacts()

    text = clean_text(bug.title + " " + bug.description)
    embeddings = embedding_model.encode([text])
    embeddings_csr = sp.csr_matrix(embeddings)

    meta = pd.DataFrame([{"component": bug.component, "version": bug.version}])
    meta_enc = sp.csr_matrix(ohe.transform(meta))

    if bug.created_time is not None or bug.created_time != "":
        dt = datetime.datetime.fromisoformat(bug.created_time)
    else:
        dt = datetime.datetime.now()

    additional_df = pd.DataFrame(
        [
            {
                "created_hour": dt.hour,
                "created_dayofweek": dt.weekday(),
                "created_month": dt.month,
                "created_year": dt.year,
                "text_length": len(text),
                "word_count": len(text.split()),
                "avg_word_length": np.mean([len(w) for w in text.split()])
                if text.split()
                else 0.0,
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

    metas = pd.DataFrame(
        [{"component": b.component, "version": b.version} for b in bugs]
    )
    meta_enc = sp.csr_matrix(ohe.transform(metas))

    rows = []
    for b, text in zip(bugs, texts):
        dt = (
            datetime.datetime.fromisoformat(b.created_time)
            if b.created_time
            else datetime.datetime.now()
        )
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


def predict(bug: BugData) -> tuple[Prediction, float]:
    start = time.perf_counter()

    x = build_features(bug)
    model = load_model()
    probability = float(model.predict_proba(x)[0, 1])
    prediction = 0 if probability < THRESHOLD else 1
    label = "Low Priority" if prediction == 0 else "High Priority"

    elapsed_ms = round((time.perf_counter() - start) * 1000, 2)
    return Prediction(
        label=label, prediction=prediction, probability=probability, threshold=THRESHOLD
    ), elapsed_ms


def predict_batch(bugs: list[BugData]) -> tuple[list[Prediction], float]:
    start = time.perf_counter()

    x = build_features_batch(bugs)
    model = load_model()
    probabilities = model.predict_proba(x)[:, 1]

    results = []
    for prob in probabilities:
        probability = float(prob)
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
