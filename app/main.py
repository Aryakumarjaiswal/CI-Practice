from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="CI Fast-API Demo")

class PredictRequest(BaseModel):
    text: str

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "FastAPI CI Pipeline"}

@app.post("/predict")
def predict_sentiment(payload: PredictRequest):
    # Dummy processing logic
    text_length = len(payload.text)
    return {
        "input_text": payload.text,
        "processed": True,
        "char_count": text_length
    }
