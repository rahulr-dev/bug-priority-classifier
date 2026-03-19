from fastapi import FastAPI
from src.models.BugData import BugData
from src.models.Prediction import Prediction
from src.utils.inference import predict, predict_batch


app = FastAPI()


@app.get("/")
def health_check():
    return {"health": "ok"}


@app.post("/predict")
def predict_priority(bug: BugData):
    result, elapsed_ms = predict(bug)
    return {"prediction": result, "inference_time_ms": elapsed_ms}


@app.post("/predict/batch")
def predict_batch_priority(bugs: list[BugData]):
    results, elapsed_ms = predict_batch(bugs)
    return {
        "predictions": results,
        "inference_time_ms": elapsed_ms,
        "count": len(results),
    }
