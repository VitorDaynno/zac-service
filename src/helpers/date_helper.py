from datetime import datetime
from dateutil import parser

from src.config.logger import logger


class DateHelper:

    def __init__(self):
        logger.info("Initialize DateHelper")

    @staticmethod
    def today():
        return datetime.now()

    @staticmethod
    def to_date(date):
        parsed_date = parser.parse(date)
        return parsed_date
