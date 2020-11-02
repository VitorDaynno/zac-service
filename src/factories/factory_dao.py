from src.daos.trello_card_dao import TrelloCardDAO
from src.helpers.db_helper import DB


class FactoryDAO:

    def __init__(self):
        self.__db = DB()

    def get_trello_card_dao(self):
        return TrelloCardDAO(self.__db)
