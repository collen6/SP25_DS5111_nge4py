""" Module auto-generated docstring """

# bin/gainers/yahoo.py
from .base import BaseGainer


class YahooGainer(BaseGainer):
    def __init__(self, url, data_file):
        super().__init__(url, data_file)

    def fetch_data(self):
        print(f"Fetching data from Yahoo: {self.url}")

    def process_data(self):
        print(f"Processing Yahoo data and saving to {self.data_file}")
