from src.config.logger import logger


class Routine:
    def __init__(self, dao, date_helper):
        logger.info("Initializing Routine")
        self._dao = dao

    def get(self, filters):
        logger.info("Initializing get routine")
        routines = self._dao.get(filters)
        return routines