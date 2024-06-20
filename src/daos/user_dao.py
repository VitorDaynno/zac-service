from src.config.logger import logger


class UserDAO:
    def __init__(self, db_helper):
        logger.info("Initializing UserDAO")
        self._db = db_helper
        self._collection = "users"

    def get(self, filters):
        logger.info("Initializing get users")

        if "id" in filters:
            id = filters.pop("id")
            filters["_id"] = self._db.to_object_id(id)

        users = self._db.get(self._collection, filters)
        return users
