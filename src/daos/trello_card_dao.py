from src.config.logger import logger


class TrelloCardDAO:
    def __init__(self, db):
        logger.info("Initializing Trello crawler")
        self._db = db
        self._collection = "trello_cards"

    def save(self, trello_card):
        logger.info("Initializing save card")
        r = self._db.insert(self._collection, trello_card)
        return r
