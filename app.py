# app.py
from fastapi import FastAPI
import pickle
import numpy as np

# Initialize app
app = FastAPI(title="Iris Classifier API", version="1.0")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def root():
    return {"status": "ok", "message": "Iris ML API is running!"}

@app.post("/predict")
def predict(features: list[float]):
    """
    Example body:
    {
      "features": [5.1, 3.5, 1.4, 0.2]
    }
    """
    prediction = model.predict([features])
    return {"prediction": int(prediction[0])}
