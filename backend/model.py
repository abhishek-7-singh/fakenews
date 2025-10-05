import joblib
import numpy as np

# Load a pre-trained fake news detection model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def fake_news_detection(text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return {"text": text, "is_fake": bool(prediction[0])}
