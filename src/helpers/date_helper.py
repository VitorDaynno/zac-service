from datetime import datetime, timedelta
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
        parsed_date = parser.parse(date)
        return parsed_date

    @staticmethod
    def add_hour(datetime, hour):
        parsed_datetime = datetime + timedelta(hours=hour)
        return parsed_datetime
