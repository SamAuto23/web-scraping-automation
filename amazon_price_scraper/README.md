Overview

The Amazon Price Scraper is a Python script designed to extract product prices from Amazon and notify users when there are price changes.

Features

Scrapes real-time product prices from Amazon.

Stores data for price tracking.

Sends notifications if prices change significantly.

Dependencies

requests

BeautifulSoup

pandas

smtplib

Usage

Install dependencies using pip install -r requirements.txt.

Configure the .env file with your email credentials.

Run python amazon_price_scraper.py to start monitoring prices.

Amazon Scraper

Overview

This script collects product details from Amazon, including price, title, and availability, and stores the information in a structured format.

Features

Extracts product details efficiently.

Saves data in a CSV or JSON format.

Uses rotating user agents to avoid detection.

Dependencies

requests

BeautifulSoup

pandas

Usage

Install dependencies using pip install -r requirements.txt.

Run python amazon_scraper.py and enter product URLs.

