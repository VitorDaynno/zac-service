import threading

from src.config.logger import logger
from src.helpers.thread_job import ThreadJob
from src.server import http_server
from src.services.trello_crawler import TrelloCrawler
from src.factories.factory_controller import FactoryController


def updated_cards():
    logger.info("Initializing updated cards")
    trello_crawler = TrelloCrawler()
    trello_crawler.integrate_cards()

def create_tasks_by_routine():
    logger.info("Initializing create tasks by routine")

    factoryController = FactoryController()
    task = factoryController.get_task()

    task.create_tasks_by_routine()


def main():
    logger.info("Initialize Zac")

    event = threading.Event()
    routine = ThreadJob(updated_cards, event, 86400)
    routine.start()

    routine_event = threading.Event()
    routine_cron = ThreadJob(create_tasks_by_routine, routine_event, 60)
    routine_cron.start()

    http_server.serve_forever()


if __name__ == '__main__':
    main()
