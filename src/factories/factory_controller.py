from src.controllers.trello_card import TrelloCard
from src.controllers.task import Task
from src.factories.factory_dao import FactoryDAO
from src.helpers.date_helper import DateHelper
from src.helpers.model_helper import ModelHelper


class FactoryController:

    def __init__(self):
        self._factory_dao = FactoryDAO()
        self._date_helper = DateHelper()
        self._model_helper = ModelHelper()

    def get_trello_card(self):
        dao = self._factory_dao.get_trello_card_dao()
        date_helper = self._date_helper
        return TrelloCard(dao, date_helper)

    def get_task(self):
        trello_card = self.get_trello_card()
        return Task(trello_card, self._model_helper)
