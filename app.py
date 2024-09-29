from flask import Flask, request, jsonify
from textblob import TextBlob

app = Flask(__name__)


reviews = [
    {
        "title": "Great phone!",
        "text": "This iPhone is amazing!",
        "storage": "128GB",
        "color": "Black",
        "rating": 5,
        "verified_purchase": True
    },
    {
        "title": "Not worth the price",
        "text": "It's okay, but overpriced.",
        "storage": "64GB",
        "color": "White",
        "rating": 3,
        "verified_purchase": False
    },
    
]


@app.route('/')
def home():
    return "Welcome to the iPhone Review API! "


@app.route('/api/sentiment', methods=['POST'])
def sentiment():
    data = request.get_json()
    review_text = data.get('review_text', '')
    sentiment_result = get_sentiment(review_text)
    return jsonify({'sentiment': sentiment_result})

def get_sentiment(review_text):
    analysis = TextBlob(review_text)
    return "positive" if analysis.sentiment.polarity > 0 else "negative"


@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    color = request.args.get('color')
    storage = request.args.get('storage')
    rating = request.args.get('rating', type=int)

    filtered_reviews = [
        review for review in reviews
        if (color is None or review['color'].lower() == color.lower()) and
           (storage is None or review['storage'] == storage) and
           (rating is None or review['rating'] == rating)
    ]

    return jsonify(filtered_reviews)

if __name__ == '__main__':
    app.run(debug=True)


