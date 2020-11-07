from src.daos.trello_card_dao import TrelloCardDAO
from src.helpers.db_helper import DBHelper
from src.helpers.date_helper import DateHelper


class FactoryDAO:

    def __init__(self):
        self._db = DBHelper()
        self._date_helper = DateHelper()

    def get_trello_card_dao(self):
        return TrelloCardDAO(self._db, self._date_helper)
