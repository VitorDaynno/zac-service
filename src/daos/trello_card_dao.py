from src.config.logger import logger


class TrelloCardDAO:
    def __init__(self, db_helper, date_helper):
        logger.info("Initializing Trello crawler")
        self._db = db_helper
        self._date_helper = date_helper
        self._collection = "trello_cards"

    def save(self, trello_card):
        logger.info("Initializing save card")
        r = self._db.insert(self._collection, trello_card)
        return r

    def get(self, filters):
        logger.info("Initializing get cards")

        search_filter = {}

        if "start_date" in filters:
            search_filter = {
                "due": {
                    "$gte": self._date_helper.to_date(filters["start_date"])
                }
            }

        if "start_date" in filters and "end_date" in filters:
            search_filter["due"]["$lte"] = self._date_helper.to_date(
                filters["end_date"]
            )

        r = self._db.get(self._collection, search_filter)
        return r

    def delete(self, filters):
        logger.info("Initializing delete cards")

        r = self._db.delete(self._collection, filters)
        return r
