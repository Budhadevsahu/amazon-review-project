import requests
from bs4 import BeautifulSoup
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["amazon_reviews"]
collection = db["iphone12_reviews"]


def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    reviews = soup.find_all('div', {'data-hook': 'review'})
    for review in reviews:
        title = review.find('a', {'data-hook': 'review-title'}).text.strip()
        text = review.find('span', {'data-hook': 'review-body'}).text.strip()
        style_name = review.find('a', {'data-hook': 'format-strip'}).text.strip()
        color = "Unknown"  
        verified = review.find('span', {'data-hook': 'avp-badge'}).text.strip() if review.find('span', {'data-hook': 'avp-badge'}) else 'No'

        
        collection.insert_one({
            "title": title,
            "text": text,
            "style_name": style_name,
            "color": color,
            "verified_purchase": verified
        })

for i in range(1, 5):
    page_url = f'https://www.amazon.in/Apple-New-iPhone-12-128GB/product-reviews/B08L5TNJHG?pageNumber={i}'
    scrape_page(page_url)

print("Scraping completed!")
