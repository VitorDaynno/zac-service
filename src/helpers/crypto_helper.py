import hashlib

from src.config.config import Config
from src.config.logger import logger


class CryptoHelper:

    def __init__(self):
        logger.info("Initialize CryptoHelper")
        self._config = Config()

    def to_sha256(self, text):
        logger.info("Initialize encoding")

        text_encoded = text.encode()
        salt = self._config.get_salt()

        text_to_transform = text_encoded + salt.encode()

        sha256_text = hashlib.sha256(text_to_transform).hexdigest()

        return sha256_text
