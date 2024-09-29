from textblob import TextBlob
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["amazon_reviews"]
collection = db["iphone12_reviews"]


def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

for review in collection.find():
    sentiment = analyze_sentiment(review['text'])
    collection.update_one({'_id': review['_id']}, {'$set': {'sentiment': sentiment}})

print("Sentiment analysis completed!")
