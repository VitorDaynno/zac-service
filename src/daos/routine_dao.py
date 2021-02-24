from src.config.logger import logger


class RoutineDAO:
    def __init__(self, db_helper, date_helper):
        logger.info("Initializing RoutineDAO")
        self._db = db_helper
        self._date_helper = date_helper
        self._collection = "routines"

    def get(self, filters):
        logger.info("Initializing get tasks")

        search_filter = {"$and": []}

        if "user" in filters:
            search_filter["$and"].append({"userId": filters["user"]})

        if "days" in filters:
            search_filter["$and"].append({"days": {"$in": filters["days"]}})

        if "isActive" in filters:
            search_filter["$and"].append({"isActive": filters["isActive"]})

        r = self._db.get(self._collection, search_filter, sort=[["date", 1]])
        return r
