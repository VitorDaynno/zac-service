import threading

from src.config.logger import logger
from src.helpers.thread_job import ThreadJob
from src.server import http_server
from src.services.trello_crawler import TrelloCrawler


def updated_cards():
    logger.info("Initializing updated cards")
    trello_crawler = TrelloCrawler()
    trello_crawler.integrate_cards()


def main():
    logger.info("Initialize Zac")

    event = threading.Event()
    routine = ThreadJob(updated_cards, event, 86400)
    routine.start()

    http_server.serve_forever()


if __name__ == '__main__':
    main()
