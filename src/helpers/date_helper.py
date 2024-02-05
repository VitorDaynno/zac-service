from datetime import datetime, timedelta
from dateutil import parser, tz

from src.config.logger import logger


class DateHelper:

    def __init__(self):
        logger.info("Initialize DateHelper")

    @staticmethod
    def now():
        return datetime.utcnow()

    @staticmethod
    def to_date(date):
        parsed_date = parser.parse(date)
        return parsed_date

    @staticmethod
    def add_hour(datetime, hour):
        parsed_datetime = datetime + timedelta(hours=hour)
        return parsed_datetime

    def initial_date(self, additional_hour=0):
        now = self.now()
        initial_date = datetime(now.year, now.month, now.day, additional_hour, 0, 0)

        return initial_date

    @staticmethod
    def to_str_date(datetime, mask="%d/%m/%Y"):
        return datetime.strftime(mask)

    @staticmethod
    def get_week_day(date):
        week_day = date.weekday()
        if week_day == 6:
            return 0
        return week_day + 1