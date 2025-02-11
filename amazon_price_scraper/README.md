# Amazon Price Scraper

## Overview
The Amazon Price Scraper is a Python script designed to extract product prices from multiple Amazon product pages. It utilises both **requests** and **Selenium** to handle Amazon’s anti-scraping mechanisms, ensuring successful data extraction.

## Features
- Scrapes multiple **Amazon product prices** in real time.
- Uses **ScraperAPI** to bypass bot detection.
- Implements **Selenium** as a backup for blocked requests.
- Includes **error handling** and **retry logic**.
- Saves data into a **CSV file** for analysis.

## Dependencies
To use this script, install the required Python libraries:

```bash
pip install requests beautifulsoup4 selenium webdriver-manager pandas


Library Descriptions:
requests – Handles HTTP requests to Amazon.
BeautifulSoup – Parses HTML content to extract product data.
selenium – Automates web interactions when requests fail.
webdriver-manager – Manages WebDriver for Selenium.
pandas – Stores and processes scraped data.

Proxy Configuration (Required)
Amazon aggressively blocks scrapers, so a proxy service is required. The script is configured to use ScraperAPI or another proxy of your choice.

Setup Instructions:
1.Sign up for a proxy service (e.g., ScraperAPI, BrightData).
2.Obtain your API key from the provider.
3.Modify the script:
Locate the PROXY_URL_TEMPLATE variable in amazon_price_scraper.py.
Replace "YOUR_PROXY_API_KEY" with your actual key.

Example setup for ScraperAPI:
PROXY_URL_TEMPLATE = "http://api.scraperapi.com/?api_key={}&url={}"


To disable the proxy, set:
USE_PROXY = False

Usage
1. Clone the repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/web-scraping-automation.git

2. Navigate to the project directory:
cd amazon_price_scraper

3. Run the script:
python amazon_price_scraper.py


Configuration
Add multiple Amazon product URLs inside the script.
Ensure ScraperAPI or a similar proxy is correctly set up.
Configure Selenium as a backup for blocked requests.
The script automatically saves results in amazon_prices.csv.
Error Handling
Retries requests up to 3 times before switching to Selenium.
Delays are added randomly to mimic human behaviour.
Handles CAPTCHAs and blocked requests.
Contributing
Feel free to submit issues, fork the repository, and make pull requests to enhance the project.

License
This project is open-source and available under the MIT License.



---

### **Why This is Perfect for GitHub:**
✅ **Clear Proxy Instructions** – Ensures users configure ScraperAPI correctly.  
✅ **Selenium Integration** – Explains fallback scraping when requests fail.  
✅ **Error Handling Section** – Highlights how the script deals with Amazon’s defences.  
✅ **Multi-Product Scraping** – Shows users how to scrape **multiple products efficiently**.  
✅ **Formatted for GitHub Readability** – Looks **clean** and **professional**.

Now **just copy and paste** this into `README.md`, and you’re done! 🚀

