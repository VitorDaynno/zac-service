from src.api import zac
from src.config.logger import logger
from src.helpers.access_helper import required_token
from src.services.trello_crawler import TrelloCrawler


@zac.route("/api/trello-crawler/integrate-cards", methods=["POST"])
@required_token
def integrate_cards():
    logger.info("Initializing updated cards")
    trello_crawler = TrelloCrawler()
    trello_crawler.integrate_cards()

    return {"message": "Done"}
