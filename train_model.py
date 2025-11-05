# train_model.py
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

# Load a built-in small dataset
X, y = load_iris(return_X_y=True)

# Train a simple model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save the trained model
pickle.dump(model, open("model.pkl", "wb"))

print(" Model trained and saved as model.pkl")
