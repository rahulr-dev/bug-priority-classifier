# Bug Priority Classifier

Predicts whether an Eclipse bug report is High Priority (P1/P2) or Low Priority (P3–P5) using sentence embeddings and XGBoost.

**Stack:** Python · XGBoost · sentence-transformers · FastAPI · Streamlit · MLflow · Docker

---

## Run with Docker

```bash
cp .env.example .env
docker-compose up --build
```

| Service | URL |
|---------|-----|
| API | http://localhost:8000 |
| UI | http://localhost:8501 |

> Requires `artifacts/` to contain `final_xgboost_path_b.pkl`, `ohe.pkl`, and `scaler.pkl`.

---

## Run Locally

```bash
pip install -r requirements.txt

uvicorn src.api.main:app --reload      # API on :8000
streamlit run src/app/app.py           # UI  on :8501
```

---

## API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/predict` | POST | Single bug prediction |
| `/predict/batch` | POST | Batch prediction |

**Request body:**
```json
{
  "title": "NullPointerException on workspace load",
  "description": "Occurs when opening a project with...",
  "component": "Runtime",
  "version": "3.0",
  "created_time": "2024-01-01T00:00:00"
}
```

---

## Reproduce the Model

```bash
jupyter notebook notebooks/research.ipynb
```

Runs EDA → cleaning → feature engineering → three modeling paths → MLflow tracking → saves artifacts to `artifacts/`.

Optionally fine-tune the embedding model:
```bash
jupyter notebook notebooks/finetune_embeddings.ipynb
```

---

## Approach

**Dataset:** Eclipse Open Source Bug Dataset, ~85k samples, 10.85:1 class imbalance (Low:High).

Each sample combines `title` + `description` into a cleaned text field. Additional features: OHE component/version, time features, text statistics — all stacked onto the text representation.

Three text representations were compared, all using XGBoost as the classifier:

| Path | Text Representation | Imbalance Strategy |
|------|--------------------|--------------------|
| A | TF-IDF (5k features, 1–2 ngrams) | SMOTE + `scale_pos_weight` |
| B | `all-MiniLM-L6-v2` base embeddings (384d) | `scale_pos_weight` |
| C | Fine-tuned `all-MiniLM-L6-v2` | `scale_pos_weight` |

XGBoost was tuned with early stopping on AUC + 100-trial Optuna HPO. Decision threshold searched over [0.1, 0.9] to maximise F1 on the minority class.

---

## Results

| Path | Text Representation | Threshold | F1 (High) | AUC-ROC |
|------|---------------------|:---------:|:---------:|:-------:|
| A | TF-IDF | 0.50 | 0.295 | 0.774 |
| **B** | **Base embeddings** | **0.58** | **0.356** | **0.813** |
| C | Fine-tuned embeddings | 0.61 | 0.351 | 0.811 |

**Path B wins.** Embeddings improved F1 by +0.061 over TF-IDF. Fine-tuning added training cost with no measurable gain (ΔAUC-ROC < 0.01). Threshold tuning from 0.5 → 0.58 added ~0.015 F1 by better balancing precision and recall on the minority class.
