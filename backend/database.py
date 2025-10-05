import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["news_db"]
collection = db["news_articles"]
