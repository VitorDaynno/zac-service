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

        if "id" in filters:
            search_filter["$and"].append({"_id": self._db.to_object_id(filters["id"])})

        if "user" in filters:
            search_filter["$and"].append({"user_id": filters["user"]})

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

        if "is_conclude" in filters:
            search_filter["$and"].append({"is_conclude": filters["is_conclude"]})

        if "is_failed" in filters:
            search_filter["$and"].append({
                "is_failed": {
                    "$ne": not filters["is_failed"]
                }
            })

        r = self._db.get(self._collection, search_filter, sort=[["date", 1]])
        return r

    def update(self, filters, entity):
        logger.info("Initializing update tasks")

        update_filter = {"$and": []}
        update_entity = {"$set": {}}

        if "id" in filters:
            update_filter["$and"].append(
                {"_id": self._db.to_object_id(filters["id"])}
                )

        if "user" in filters:
            update_filter["$and"].append({"user_id": filters["user"]})

        if "name" in entity:
            update_entity["$set"]["name"] = entity["name"]

        if "date" in entity:
            update_entity["$set"]["date"] = entity["date"]

        if "start_time" in entity:
            update_entity["$set"]["start_time"] = entity["start_time"]

        if "end_time" in entity:
            update_entity["$set"]["end_time"] = entity["end_time"]

        if "note" in entity:
            update_entity["$set"]["note"] = entity["note"]

        if "is_conclude" in entity:
            update_entity["$set"]["is_conclude"] = entity["is_conclude"]

        if "is_failed" in entity:
            update_entity["$set"]["is_failed"] = entity["is_failed"]

        if "is_enabled" in entity:
            update_entity["$set"]["is_enabled"] = entity["is_enabled"]

        r = self._db.update(self._collection, update_filter, update_entity)
        return r

    def insert(self, task):
        logger.info("Initializing create task")

        r = self._db.insert(self._collection, task)

        return r