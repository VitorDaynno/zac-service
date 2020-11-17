from src.config.logger import logger


class ZacTask:
    def __init__(self, dao, date_helper):
        logger.info("Initializing ZacTask")
        self._dao = dao

    def get(self, filters):
        logger.info("Initializing get cards")
        cards = self._dao.get(filters)
        return cards
