from src.config.logger import logger
from src.config.config import Config
from src.factories.factory_controller import FactoryController
from src.helpers.request_helper import RequestHelper
from src.helpers.date_helper import DateHelper


class TrelloCrawler:
    def __init__(self):
        logger.info("Initializing Trello crawler")

        factory_controller = FactoryController()
        self._config = Config()
        self._request_helper = RequestHelper()
        self._date_helper = DateHelper()

        self._trello_card_controller = factory_controller.get_trello_card()

    def integrate_cards(self):
        logger.info("Initializing integration of cards")
        self._trello_card_controller.delete({})
        boards = self.get_boards()

        self.process_boards(boards)

    def get_boards(self):
        logger.info("Initializing get boards")
        url = self._config.get_boards_url()
        params = self._config.get_trello_auth()

        boards = self._request_helper.get(url, params)

        return boards

    def process_boards(self, boards):
        logger.info("Initializing process boards")
        for board in boards:
            id = board["shortLink"]
            is_closed = board["closed"]

            if not is_closed:
                self.process_cards(id)

    def process_cards(self, board_id):
        logger.info("Initializing process cards")
        cards = self.get_cards(board_id)
        cards = self.format_cards(cards)

        self.save_cards(cards)

    def get_cards(self, board_id):
        logger.info("Initializing get cards by {}".format(board_id))

        url = self._config.get_cards_url()
        params = self._config.get_trello_auth()

        url = url.format(board_id)

        cards = self._request_helper.get(url, params)

        return cards

    def format_cards(self, cards):
        logger.info("Initializing format cards")

        user_id = self._config.get_trello_user()
        formatted_cards = []

        for card in cards:
            name = card["name"]
            url = card["url"]
            member_id = card["idMembers"][0] if len(
                card["idMembers"]) > 0 else None
            due = card["due"]
            due_complete = card["dueComplete"]

            if user_id == member_id and due is not None and not due_complete:
                due = self._date_helper.to_date(due)

                formatted_card = {
                    "name": name,
                    "due": due,
                    "url": url,
                    "user": user_id
                }

                formatted_cards.append(formatted_card)

        return formatted_cards

    def save_cards(self, cards):
        logger.info("Initializing save cards")

        for card in cards:
            self._trello_card_controller.save(card)
