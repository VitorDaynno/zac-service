from src.config.logger import logger
from src.helpers.error_helper import UnprocessableEntity


class Routine:
    def __init__(self, dao, date_helper, model_helper):
        logger.info("Initializing Routine")
        self._dao = dao
        self._date_helper = date_helper
        self._model_helper = model_helper

    def get(self, filters):
        logger.info("Initializing get routine")
        routines = self._dao.get(filters)
        return routines

    def create(self, user, entity):
        try:
            logger.info("Saving routine '{0}'".format(entity))

            self.verify(entity)

            routine = {
                "name": entity["name"],
                "days": entity["days"],
                "start_time": self._date_helper.to_str_date(
                    self._date_helper.to_local_date(
                        entity["startTime"],
                        user["timezone"]
                    ),
                    "%H:%M"
                ),
                "end_time": self._date_helper.to_str_date(
                    self._date_helper.to_local_date(
                        entity["endTime"],
                        user["timezone"]
                    ),
                    "%H:%M"
                ),
                "user_id": user["id"],
                "is_active": True,
                "is_enabled": True
            }

            id = self._dao.insert(routine)

            created_routine = self.get_by_id(id)

            return self._model_helper.zac_routines(created_routine)[0]
        except Exception as error:
            logger.error("An error occurred: {0}".format(error))
            raise error

    def verify(self, routine):
        if "name"  not in routine:
            raise UnprocessableEntity("name is required")

        if "days" not in routine:
            raise UnprocessableEntity("days is required")

        if "startTime" not in routine:
            raise UnprocessableEntity("startTime is required")

        if "endTime" not in routine:
            raise UnprocessableEntity("endTime is required")

    def get_pending_routines(self):
        logger.info("Starting get pending routines")

        today = self._date_helper.initial_date(0)

        search_filter = {
            "$or": [
                {
                    "last_created_date": {
                        "$lt": today
                    }
                },
                {
                    "last_created_date": {
                        "$exists": False
                    }
                }
            ],
            "is_active": True,
            "is_enabled": True
        }

        routines = self._dao.get_by_filter(search_filter)

        return routines

    def get_by_id(self, id):
        logger.info("Initializing get by id")
        routine = self._dao.get({ "id": id })

        return routine

    def update_last_created_date(self, routine_id, date):
        logger.info("Updating date in routine {0}".format(routine_id))
        self._dao.update_last_created_date(routine_id, date)