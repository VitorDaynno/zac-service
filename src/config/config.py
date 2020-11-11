import os
import sys
from dotenv import load_dotenv

from src.config.logger import logger


class Config:

    def __init__(self):
        logger.info("Starting Config")
        load_dotenv()

    def get_boards_url(self):
        logger.info("Getting boards' url from enviroment")
        board_url = self.get_variable_by_environment("BOARDS_URL")
        logger.info("Get boards' url  with success")
        return board_url

    def get_trello_auth(self):
        logger.info("Getting trello's auth ")
        key = self.get_trello_key()
        token = self.get_trello_token()

        params = {
            "key": key,
            "token": token
        }

        return params

    def get_trello_key(self):
        logger.info("Getting Trello's key from enviroment")
        trello_key = self.get_variable_by_environment("TRELLO_KEY")
        logger.info("Get Trello's key with success")
        return trello_key

    def get_trello_token(self):
        logger.info("Getting Trello's token from enviroment")
        trello_token = self.get_variable_by_environment("TRELLO_TOKEN")
        logger.info("Get Trello's token with success")
        return trello_token

    def get_cards_url(self):
        logger.info("Getting cards' url from enviroment")
        cards_url = self.get_variable_by_environment("CARDS_URL")
        logger.info("Get cards' url with success")
        return cards_url

    def get_trello_user(self):
        logger.info("Getting trello's user from enviroment")
        trello_user = self.get_variable_by_environment("TRELLO_USER")
        logger.info("Get trello's user with success")
        return trello_user

    def get_db_server(self):
        logger.info("Getting db's server from enviroment")
        db_server = self.get_variable_by_environment("DB_SERVER")
        logger.info("Get db's server with success")
        return db_server

    def get_db_port(self):
        logger.info("Getting db's port from enviroment")
        db_port = self.get_variable_by_environment("DB_PORT")
        logger.info("Get db's port with success")
        return int(db_port)

    def get_db_database(self):
        logger.info("Getting db's database from enviroment")
        db_database = self.get_variable_by_environment("DB_DATABASE")
        logger.info("Get db's database with success")
        return db_database

    def get_zac_host(self):
        logger.info("Getting zac's host from enviroment")
        zac_host = self.get_variable_by_environment("ZAC_HOST")
        logger.info("Get zac's host with success")
        return zac_host

    def get_zac_port(self):
        logger.info("Getting zac's port from enviroment")
        zac_port = self.get_variable_by_environment("ZAC_PORT")
        logger.info("Get zac's port with success")
        return int(zac_port)

    def get_salt(self):
        logger.info("Getting zac's salt from enviroment")
        zac_salt = self.get_variable_by_environment("ZAC_SALT")
        logger.info("Get zac's salt with success")
        return zac_salt

    def get_jwt_secret(self):
        logger.info("Getting jwt's secret from enviroment")
        jwt_secret = self.get_variable_by_environment("JWT_SECRET")
        logger.info("Get jwt's secret with success")
        return jwt_secret

    def get_jwt_algorithm(self):
        logger.info("Getting jwt's algorithm from enviroment")
        jwt_algorithm = self.get_variable_by_environment("JWT_ALGORITHM")
        logger.info("Get jwt's algorithm with success")
        return jwt_algorithm

    @staticmethod
    def get_variable_by_environment(variable_name):
        variable_value = os.getenv(variable_name)
        if variable_value is None:
            logger.error("{0} not found".format(variable_name))
            sys.exit()
        return variable_value
