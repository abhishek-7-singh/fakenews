import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn

# Load dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("cleaned - cleaned.csv")  # Ensure this dataset exists
X = df["title"]
y = df["text"]

# Text preprocessing
vectorizer = TfidfVectorizer(stop_words="english", max_df=0.7)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Save with protocol to avoid compatibility issues
joblib.dump(vectorizer, "vectorizer.pkl", protocol=4)
joblib.dump(model, "fake_news_model.pkl", protocol=4)

print("Model retrained and saved successfully!")
