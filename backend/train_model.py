import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib
import os

os.makedirs("models", exist_ok=True)

csv_path = "features/landmarks.csv"
if not os.path.exists(csv_path):
    raise SystemExit("Run extract_features.py first. landmarks.csv missing.")

df = pd.read_csv(csv_path)

X = df[[c for c in df.columns if c.startswith("f")]].values
y = df["label"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred))

joblib.dump(clf, "models/rf_signs.pkl")
print("Model saved to models/rf_signs.pkl")

cm = confusion_matrix(y_test, y_pred, labels=clf.classes_)
cm_df = pd.DataFrame(cm, index=clf.classes_, columns=clf.classes_)
cm_df.to_csv("features/confusion_matrix.csv")
print("Confusion matrix saved to features/confusion_matrix.csv")
