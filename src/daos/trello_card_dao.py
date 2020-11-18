from src.config.logger import logger


class TrelloCardDAO:
    def __init__(self, db_helper, date_helper):
        logger.info("Initializing TrelloCardDAO")
        self._db = db_helper
        self._date_helper = date_helper
        self._collection = "trello_cards"

    def save(self, trello_card):
        logger.info("Initializing save card")
        r = self._db.insert(self._collection, trello_card)
        return r

    def get(self, filters):
        logger.info("Initializing get cards")

        search_filter = {"$and": []}

        if "user" in filters:
            search_filter["$and"].append({"user": filters["user"]})

        if "start_date" in filters or "end_date" in filters:
            date_filter = {"due": {}}
            if "start_date" in filters:
                date_filter["due"]["$gte"] = self._date_helper.to_date(
                    filters["start_date"])

            if "end_date" in filters:
                date_filter["due"]["$lte"] = self._date_helper.to_date(
                    filters["end_date"]
                )

            search_filter["$and"].append(date_filter)

        r = self._db.get(self._collection, search_filter, sort=[["due", 1]])
        return r

    def delete(self, filters):
        logger.info("Initializing delete cards")

        r = self._db.delete(self._collection, filters)
        return r
