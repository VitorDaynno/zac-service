from src.controllers.trello_card import TrelloCard
from src.controllers.task import Task
from src.controllers.user import User
from src.factories.factory_dao import FactoryDAO
from src.helpers.crypto_helper import CryptoHelper
from src.helpers.date_helper import DateHelper
from src.helpers.model_helper import ModelHelper
from src.helpers.jwt_helper import JWTHelper


class FactoryController:

    def __init__(self):
        self._factory_dao = FactoryDAO()
        self._date_helper = DateHelper()
        self._model_helper = ModelHelper()
        self._crypto_helper = CryptoHelper()
        self._jwt_helper = JWTHelper()

    def get_trello_card(self):
        dao = self._factory_dao.get_trello_card_dao()
        date_helper = self._date_helper
        return TrelloCard(dao, date_helper)

    def get_task(self):
        trello_card = self.get_trello_card()
        return Task(trello_card, self._model_helper)

    def get_user(self):
        dao = self._factory_dao.get_user_dao()
        return User(
            dao,
            self._date_helper,
            self._crypto_helper,
            self._model_helper,
            self._jwt_helper
        )
