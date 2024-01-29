from src.config.logger import logger


class RoutineDAO:
    def __init__(self, db_helper, date_helper):
        logger.info("Initializing RoutineDAO")
        self._db = db_helper
        self._date_helper = date_helper
        self._collection = "routines"

    def get(self, filters):
        logger.info("Initializing get routine")

        search_filter = {"$and": []}

        if "id" in filters:
            search_filter["$and"].append({"_id": self._db.to_object_id(filters["id"])})

        if "user" in filters:
            search_filter["$and"].append({"user_id": filters["user"]})

        if "days" in filters:
            search_filter["$and"].append({"days": {"$in": filters["days"]}})

        if "isActive" in filters:
            search_filter["$and"].append({"is_active": filters["isActive"]})

        r = self._db.get(self._collection, search_filter, sort=[["date", 1]])
        return r

    def get_by_filter(self, filters):
        logger.info("Initializing get routine by filter")

        r = self._db.get(self._collection, filters, sort=[["date", 1]])
        return r

    def insert(self, routine):
        logger.info("Initializing create routine")

        r = self._db.insert(self._collection, routine)

        return r

    def update_last_created_date(self, routine_id, date):
        logger.info("Updating date in routine {0}".format(routine_id))

        r = self._db.update_one(
            self._collection,
            routine_id,
            { "$set": { "last_created_date": date } }
        )

        return r