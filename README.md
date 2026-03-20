# Bug Priority Classifier

Predicts whether an Eclipse bug report is High Priority (P1/P2) or Low Priority (P3–P5) using NLP and gradient boosting.

---

## Tools & Skills

**Languages & Frameworks:** Python, FastAPI, Streamlit
**ML / NLP:** XGBoost, scikit-learn, sentence-transformers (`all-MiniLM-L6-v2`), imbalanced-learn (SMOTE), Optuna
**Experiment Tracking:** MLflow (SQLite backend, Model Registry)
**Data:** pandas, NumPy, scipy

---

## Install

```bash
git clone https://github.com/rahulr-dev/bug-priority-classifier.git
cd bug-priority-classifier
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

> Requires CUDA-compatible GPU for embedding encoding. CPU fallback works but is slower.

---

## Reproducing the Project

### 1. Prepare data

Place the raw Eclipse dataset at `data/raw/eclipse_dataset.csv`.

### 2. Run the research notebook

```bash
jupyter notebook notebooks/research.ipynb
```

Executes end-to-end: EDA → cleaning → feature engineering → Paths A / B / C → MLflow logging → artifact export to `artifacts/`.

### 3. (Optional) Fine-tune embeddings

```bash
jupyter notebook notebooks/finetune_embeddings.ipynb
```

Trains a CosineSimilarityLoss fine-tuned variant of `all-MiniLM-L6-v2`. Output saved to `artifacts/finetuned_embedding_model/`.

### 4. Register the model in MLflow

```bash
mlflow ui  # http://127.0.0.1:5000
```

Promote the winning run to the Model Registry under alias `champion`:
`models:/XGBoostModel@champion`

### 5. Start the API

```bash
uvicorn src.api.main:app --reload
```

Endpoints: `POST /predict`, `POST /predict/batch`

### 6. Start the Streamlit UI

```bash
streamlit run src/app/app.py
```

Single prediction form + batch CSV upload with downloadable results.

---

## Approach

### Dataset

**Eclipse Open Source Bug Dataset** — ~85,000 samples
Target: `1` = High (P1/P2), `0` = Low (P3/P4/P5)
Class imbalance: ~10.85:1 (Low:High)

### Cleaning

- Combined `title` + `description` into a single `text` field
- Stripped bug IDs, timestamps, name prefixes, special characters
- Dropped target-leaking columns (`status`, `resolution`, `resolved_time`)

### Feature Engineering

All paths share these additional features, stacked onto the text representation:

| Feature Group | Features |
|---------------|----------|
| Categorical | OHE `component` + `version` (64 dims) |
| Time | `created_hour`, `created_dayofweek`, `created_month`, `created_year` |
| Text stats | `text_length`, `word_count`, `avg_word_length` |

### Three Modeling Paths

| Path | Text Representation | Imbalance Strategy |
|------|--------------------|--------------------|
| A | TF-IDF (5k features, 1–2 ngrams) | SMOTE + `scale_pos_weight` |
| B | `all-MiniLM-L6-v2` base embeddings (384d) | `scale_pos_weight` |
| C | Fine-tuned `all-MiniLM-L6-v2` (CosineSimilarityLoss) | `scale_pos_weight` |

Models evaluated per path: Logistic Regression, Random Forest, XGBoost. XGBoost won all paths.

### Tuning

- **Early stopping** on AUC during XGBoost training
- **Threshold search** over [0.1, 0.9] to maximise F1 on the minority class (default 0.5 is suboptimal under heavy imbalance)
- **Optuna HPO** — 100-trial Bayesian search on Path B (`max_depth`, `learning_rate`, `subsample`, `colsample_bytree`, `min_child_weight`, `gamma`)

---

## Results & Findings

### Best Model Per Path

| Path | Model | Threshold | Precision (Hi) | Recall (Hi) | F1 (Hi) | AUC-ROC |
|------|-------|:---------:|:--------------:|:-----------:|:-------:|:-------:|
| A — TF-IDF | LR (balanced) | 0.50 | 0.189 | 0.677 | 0.295 | 0.774 |
| **B — Base Embeddings** | **XGBoost Tuned** | **0.58** | **0.272** | **0.514** | **0.356** | **0.813** |
| C — Fine-tuned Embeddings | XGBoost Tuned | 0.61 | 0.267 | 0.511 | 0.351 | 0.811 |

**Winner: Path B** — Base `all-MiniLM-L6-v2` embeddings + early-stopping XGBoost + threshold tuning.

### Key Findings

- **Embeddings beat TF-IDF** — Path B improved F1 by +0.061 and AUC-ROC by +0.038 over the best TF-IDF model.
- **Fine-tuning did not help** — Path C matched but did not exceed Path B (ΔAUC-ROC < 0.01). Base embeddings are sufficient; fine-tuning adds training cost with no measurable gain.
- **Threshold matters** — Raising the decision threshold from 0.5 → 0.58 improved F1 by ~0.015 by trading recall for precision on the minority class.
- **Random Forest consistently collapsed** — High precision, near-zero recall across all paths; not suitable for this imbalanced setup without further tuning.
- **Class imbalance is the dominant challenge** — At 10.85:1, F1 of 0.356 reflects the ceiling given the signal available in text alone.
