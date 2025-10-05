import requests
import json
import pymongo
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from news_scraper import fetch_news
from model import fake_news_detection
from text_match import text_similarity
from database import collection

app = Flask(__name__)

@app.route("/get_news", methods=["GET"])
def get_news():
    news_articles = fetch_news()
    return jsonify(news_articles)

@app.route("/check_news", methods=["POST"])
def check_news():
    data = request.json
    news_text = data.get("text", "")
    result = fake_news_detection(news_text)
    return jsonify(result)

@app.route("/match_news", methods=["POST"])
def match_news():
    data = request.json
    input_text = data.get("text", "")
    result = text_similarity(input_text)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
