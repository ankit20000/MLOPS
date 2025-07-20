from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load data
X, y = load_iris(return_X_y=True)

# Train model
clf = LogisticRegression(max_iter=200)
clf.fit(X, y)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(clf, "model/model.pkl")

print("✅ Model saved to model/model.pkl")
