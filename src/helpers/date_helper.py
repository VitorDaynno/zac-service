from datetime import datetime, timedelta, timezone
from dateutil import parser

from src.config.logger import logger


class DateHelper:

    def __init__(self):
        logger.info("Initialize DateHelper")

    @staticmethod
    def now():
        return datetime.utcnow()

    @staticmethod
    def to_date(date):
        parsed_date = parser.parse(date).astimezone(timezone.utc)
        return parsed_date

    @staticmethod
    def to_local_date(date, interval):
        local_timedelta = timedelta(hours=interval)
        local_timezone = timezone(local_timedelta)
        parsed_date = parser.parse(date).replace(tzinfo=timezone.utc).astimezone(local_timezone)
        return parsed_date

    @staticmethod
    def add_hour(datetime, hour):
        parsed_datetime = datetime + timedelta(hours=hour)
        return parsed_datetime

    def initial_date(self, time_variation):
        now = self.now()

        local_timedelta = timedelta(hours=time_variation)
        local_timezone = timezone(local_timedelta)

        initial_date = datetime(
            now.year, now.month, now.day, 0, 0, 0
        ).replace(tzinfo=timezone.utc).astimezone(local_timezone)

        return initial_date

    @staticmethod
    def to_str_date(datetime, mask="%d/%m/%Y"):
        return datetime.strftime(mask)

    @staticmethod
    def get_week_day(date, time_variation):
        local_timedelta = timedelta(hours=time_variation)
        local_timezone = timezone(local_timedelta)

        week_day = date.replace(tzinfo=timezone.utc).astimezone(local_timezone).weekday()
        if week_day == 6:
            return 0
        return week_day + 1

    @staticmethod
    def timezone_to_hour(timezone):
        signal = "-" if timezone < 0 else ""

        if abs(timezone) < 10:
            return "{0}0{1}:00".format(signal, abs(timezone))

        return "{0}{1}:00".format(signal, str(abs(timezone)))