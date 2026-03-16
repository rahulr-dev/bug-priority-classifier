from pydantic import BaseModel


class Prediction(BaseModel):
    label: str
    prediction: int
    probability: float
    threshold: float
