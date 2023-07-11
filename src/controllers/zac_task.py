from src.config.logger import logger
from src.helpers.error_helper import UnprocessableEntity


class ZacTask:
    def __init__(self, dao, date_helper):
        logger.info("Initializing ZacTask")
        self._dao = dao
        self._date_helper = date_helper

    def get(self, filters):
        logger.info("Initializing get cards")
        cards = self._dao.get(filters)

        return cards
    
    def get_by_id(self, id):
        logger.info("Initializing get by id")
        cards = self._dao.get({ "id": id })

        return cards

    def update(self, filters, entity):
        logger.info("Initializing update cards")

        if "date" in entity:
            entity["date"] = self._date_helper.to_date(entity["date"])

        if "startTime" in entity:
            entity["startTime"] = self._date_helper.to_date(entity["startTime"])

        if "endTime" in entity:
            entity["endTime"] = self._date_helper.to_date(entity["endTime"])

        self._dao.update(filters, entity)

        return self.get_by_id(filters["id"])

    def create(self, entity):
        logger.info("Initializing create task")

        self.verify_task(entity)

        task = {
            "name": entity["name"],
            "date": self._date_helper.to_date(entity["date"]),
            "start_time":  self._date_helper.to_date(entity["startTime"]),
            "end_time": self._date_helper.to_date(entity["endTime"]),
            "note": entity["note"],
            "is_conclude": False,
            "is_failed": False,
        }

        created_task_id = self._dao.insert(task)

        return self.get_by_id(created_task_id)

    def verify_task(self, task):
        if not task["name"]:
            raise UnprocessableEntity("Name is required")

        if not task["date"]:
            raise UnprocessableEntity("Date is required")

        if not task["startTime"]:
            raise UnprocessableEntity("StartTime is required")

        if not task["endTime"]:
            raise UnprocessableEntity("EndTime is required")