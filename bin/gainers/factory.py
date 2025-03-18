""" Module auto-generated docstring """

import os
import time
from datetime import datetime
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class GainersFactory:
    def __init__(self, source):
        self.source = source.lower()
        self.url = self._get_url()

    def _get_url(self):
        if self.source == "yahoo":
            return "https://finance.yahoo.com/gainers"
        elif self.source == "wsj":
            return "https://www.wsj.com/market-data/stocks/us/movers"
        else:
            raise ValueError(f"Unknown source: {self.source}")

    def fetch(self):
        # If WSJ, use headless browser
        if self.source == "wsj":
            print(
                f"Using Selenium headless browser for {self.source.upper()} fetch...")

            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            # ✅ Points to installed chromium
            chrome_options.binary_location = "/usr/bin/chromium-browser"

            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)
            time.sleep(5)  # Wait for JS to load
            html = driver.page_source
            driver.quit()

        # If Yahoo, use requests
        else:
            print(f"Fetching data from {self.source.capitalize()}: {self.url}")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                              "AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/119.0 Safari/537.36"
            }
            response = requests.get(self.url, headers=headers, timeout=10)
            if response.status_code != 200:
                print(
                    f"Failed to fetch data from {self.source}, status code: {response.status_code}")
                return
            html = response.text

        # Process the HTML to extract tables
        try:
            tables = pd.read_html(html)
            if not tables:
                print("No tables found.")
                return

            # Save the first table
            os.makedirs("sample_data", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M")
            filename = f"sample_data/{self.source}_gainers_{timestamp}.csv"
            tables[0].to_csv(filename, index=False)
            print(f"Data saved to {filename}")

        except Exception as e:
            print(f"Failed to process data: {e}")
