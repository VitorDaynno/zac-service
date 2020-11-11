import jwt

from src.config.config import Config
from src.config.logger import logger
from src.helpers.date_helper import DateHelper


class JWTHelper:
    def __init__(self):
        logger.info("Initialize JWTHelper")
        config = Config()
        self._secret = config.get_jwt_secret()
        self._algorithm = config.get_jwt_algorithm()
        self._date_helper = DateHelper()

    def encode_token(self, entity):
        now = self._date_helper.now()
        entity["exp"] = self._date_helper.add_hour(now, 1)

        encode_token = jwt.encode(
            entity, self._secret, algorithm=self._algorithm)
        return encode_token.decode("utf-8")

    def decode_token(self, token):
        decoded = jwt.decode(token, self._secret, algorithm=self._algorithm)
        return decoded
