from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import Model
from .schemas import PredictRequest, PredictResponse

app = FastAPI(title="ML service")

MODEL = Model(model_path="model/model.pt")

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    try:
        preds = MODEL.predict(req.input)
        return PredictResponse(predictions=preds)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))