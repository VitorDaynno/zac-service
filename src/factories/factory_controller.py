from src.controllers.trello_card import TrelloCard
from src.factories.factory_dao import FactoryDAO
from src.helpers.date_helper import DateHelper


class FactoryController:

    def __init__(self):
        self._factory_dao = FactoryDAO()
        self._date_helper = DateHelper()

    def get_trello_card(self):
        dao = self._factory_dao.get_trello_card_dao()
        date_helper = self._date_helper
        return TrelloCard(dao, date_helper)
