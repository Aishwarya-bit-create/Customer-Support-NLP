import random
import pandas as pd

categories = {
    "Order Issue": ["Where is my order?", "Order not delivered", "Track my order"],
    "Payment Issue": ["Payment failed", "Money deducted", "Payment error"],
    "Refund": ["I want refund", "Refund not received", "Cancel and refund"],
    "Account Issue": ["Cannot login", "Forgot password", "Account locked"],
    "Product Complaint": ["Product damaged", "Wrong product received", "Poor quality"],
    "Delivery Issue": ["Delivery delayed", "Courier lost package", "Reschedule delivery"]
}

data = []

for category, texts in categories.items():
    for _ in range(100):
        data.append([random.choice(texts), category])

df = pd.DataFrame(data, columns=["text", "category"])
df.to_csv("dataset.csv", index=False)

print("Dataset Created")