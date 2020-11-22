from src.daos.trello_card_dao import TrelloCardDAO
from src.daos.user_dao import UserDAO
from src.daos.zac_task_dao import ZacTaskDAO
from src.helpers.db_helper import DBHelper
from src.helpers.date_helper import DateHelper


class FactoryDAO:

    def __init__(self):
        self._db = DBHelper()
        self._date_helper = DateHelper()

    def get_trello_card_dao(self):
        return TrelloCardDAO(self._db, self._date_helper)

    def get_user_dao(self):
        return UserDAO(self._db)

    def get_zac_task_dao(self):
        return ZacTaskDAO(self._db, self._date_helper)
