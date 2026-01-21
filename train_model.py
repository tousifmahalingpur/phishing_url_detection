import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from feature_extraction import extract_features

# Load dataset
data = pd.read_csv("dataset/phishing.csv")

X = data["url"].apply(lambda x: extract_features(x))
X = list(X)
y = data["label"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Balanced Random Forest
model = RandomForestClassifier(
    n_estimators=200,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)

# Save model
with open("model/phishing_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved successfully")
