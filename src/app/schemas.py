from pydantic import BaseModel
from typing import List


class PredictRequest(BaseModel):
    input: List[float]


class PredictResponse(BaseModel):
    predictions: List[float]
