import requests
from bs4 import BeautifulSoup
import csv

# Set headers to mimic a browser visit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# URL of an Amazon product (change this for different products)
URL = "https://www.amazon.co.uk/dp/B08N5WRWNW"

def scrape_amazon_product(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("span", {"id": "productTitle"}).text.strip()
    price = soup.find("span", {"class": "a-price-whole"})
    rating = soup.find("span", {"class": "a-icon-alt"})

    price = price.text.strip() if price else "N/A"
    rating = rating.text.strip() if rating else "N/A"

    return {"Title": title, "Price": price, "Rating": rating}

# Scrape product data
product_data = scrape_amazon_product(URL)

# Save to CSV
with open("amazon_prices.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Rating"])
    writer.writeheader()
    writer.writerow(product_data)

print("✅ Data saved to amazon_prices.csv")

