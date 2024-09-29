# Amazon Review Analysis Project
This project scrapes reviews for the iPhone 12 from Amazon, performs sentiment analysis on those reviews, and provides APIs for review retrieval and sentiment analysis.

## Setup Instructions
1. Clone the repository or download the project files.
2. Navigate to the project folder.
3. Create a virtual environment: python -m venv venv
4. Activate the virtual environment:venv\Scripts\activate # Windows
5. Install the required packages: pip install -r requirements.txt
6. Run the application: python app.py

## API Endpoints
### Sentiment Analysis API
- **Endpoint**: `/api/sentiment`
- **Method**: POST
- **Request Body**:
  ```json
  {
    "review_text": "Your review text here"
  }
Response:
{
  "sentiment": "positive" or "negative"
}

Review Retrieval API
Endpoint: /api/reviews
Method: GET
Parameters: color, storage, rating

 List Dependencies

1:List Required Packages
- Flask
- BeautifulSoup
- Requests

