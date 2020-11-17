from src.config.logger import logger


class ZacTaskDAO:
    def __init__(self, db_helper, date_helper):
        logger.info("Initializing ZacTaskDAO")
        self._db = db_helper
        self._date_helper = date_helper
        self._collection = "tasks"

    def get(self, filters):
        logger.info("Initializing get tasks")

        search_filter = {"$and": []}

        if "usuId" in filters:
            search_filter["$and"].append({"user": filters["user"]})

        if "start_date" in filters or "end_date" in filters:
            date_filter = {"date": {}}
            if "start_date" in filters:
                date_filter["date"]["$gte"] = self._date_helper.to_date(
                    filters["start_date"])

            if "end_date" in filters:
                date_filter["date"]["$lte"] = self._date_helper.to_date(
                    filters["end_date"]
                )

            search_filter["$and"].append(date_filter)

        if "isConclude" in filters:
            search_filter["$and"].append({"isConclude": filters["isConclude"]})

        r = self._db.get(self._collection, search_filter, sort=[["date", 1]])
        return r
