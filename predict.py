import joblib
from preprocess import preprocess_text

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

responses = {
    "Order Issue": "Please check order tracking.",
    "Payment Issue": "Try another payment method.",
    "Refund": "Refund will be processed soon.",
    "Account Issue": "Reset your password.",
    "Product Complaint": "Upload product image.",
    "Delivery Issue": "Delivery will be rescheduled."
}

def predict_query(text):
    clean = preprocess_text(text)
    vector = vectorizer.transform([clean])

    category = model.predict(vector)[0]
    confidence = max(model.predict_proba(vector)[0])

    return category, responses[category], confidence
