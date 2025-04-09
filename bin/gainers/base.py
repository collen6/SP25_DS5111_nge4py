# bin/gainers/base.py
import logging


class BaseGainer:
    def __init__(self, url, data_file):
        """
        Initializes the BaseGainer with URL and data file path.

        Args:
            url (str): The URL to fetch data from.
            data_file (str): The file where the processed data will be saved.
        """
        self.url = url
        self.data_file = data_file

    def fetch_data(self):
        """
        Fetches the data from the specified URL.
        This is a placeholder method, meant to be overridden in subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def process_data(self):
        """
        Processes the fetched data and saves it to the specified data file.
        This is a placeholder method, meant to be overridden in subclasses.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def log(self, message):
        """
        A simple logging method to log messages.

        Args:
            message (str): The message to log.
        """
        logging.info(message)
