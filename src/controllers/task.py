from src.config.logger import logger


class Task:
    def __init__(self, trello_card_controller, model_helper):
        logger.info("Initializing Tasks")
        self._trello_card_controller = trello_card_controller
        self._model_helper = model_helper

    def get(self, query):
        logger.info("Initializing get tasks")

        trello_cards = self._trello_card_controller.get(query)

        cards = self._model_helper.trello_cards(trello_cards)

        return {"tasks": cards}
