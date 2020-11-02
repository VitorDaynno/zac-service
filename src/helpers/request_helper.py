import requests

from src.config.logger import logger
from src.config.config import Config


class RequestHelper:

    def __init__(self):
        self.config = Config()
        logger.info("Initialize RequestHelper")

    def get(self, url, params={}):
        headers = {
            "Accept": "application/json"
        }

        response = requests.request("GET", url, headers=headers, params=params)

        return response.json()
