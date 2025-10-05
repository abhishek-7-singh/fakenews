import requests
from database import collection
from config import NEWS_API_KEY, NEWS_API_URL

def fetch_news():
    response = requests.get(NEWS_API_URL)
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data["articles"]
        collection.insert_many(articles)  # Store in database
        return articles
    return []
