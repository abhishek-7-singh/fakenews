from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from database import collection

def text_similarity(input_text):
    stored_news = collection.find()
    news_texts = [article["title"] for article in stored_news if "title" in article]
    
    if not news_texts:
        return {"input": input_text, "match_score": 0}

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([input_text] + news_texts)
    similarity_scores = cosine_similarity(vectors[0:1], vectors[1:])

    max_score = max(similarity_scores[0]) if similarity_scores.size else 0
    return {"input": input_text, "match_score": max_score}
