from src.controllers.trello_card import TrelloCard
from src.controllers.task import Task
from src.controllers.user import User
from src.controllers.zac_task import ZacTask
from src.controllers.routine import Routine
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
        zac_task = self.get_zac_task()
        routine = self.get_routine()

        return Task(
            trello_card,
            zac_task,
            routine,
            self._model_helper,
            self._date_helper
        )

    def get_user(self):
        dao = self._factory_dao.get_user_dao()
        return User(
            dao,
            self._date_helper,
            self._crypto_helper,
            self._model_helper,
            self._jwt_helper
        )

    def get_zac_task(self):
        dao = self._factory_dao.get_zac_task_dao()
        date_helper = self._date_helper
        return ZacTask(dao, date_helper)

    def get_routine(self):
        dao = self._factory_dao.get_routine_dao()
        date_helper = self._date_helper
        model_helper = self._model_helper

        return Routine(dao, date_helper, model_helper)
