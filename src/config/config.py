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

    @staticmethod
    def get_variable_by_environment(variable_name):
        variable_value = os.getenv(variable_name)
        if variable_value is None:
            logger.error("{0} not found".format(variable_name))
            sys.exit()
        return variable_value
