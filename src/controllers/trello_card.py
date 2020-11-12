from src.config.logger import logger


class TrelloCard:
    def __init__(self, dao, date_helper):
        logger.info("Initializing TrelloCard")
        self._dao = dao
        self._date_helper = date_helper

    def save(self, trello_card):
        logger.info("Initializing save a card")

        trello_card["created_date"] = self._date_helper.now()
        self._dao.save(trello_card)

    def get(self, filters):
        logger.info("Initializing get cards")
        cards = self._dao.get(filters)
        return cards

    def delete(self, filters):
        logger.info("Initializing delete cards")
        self._dao.delete(filters)
