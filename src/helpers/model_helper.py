from src.config.logger import logger


class ModelHelper:
    def __init__(self):
        logger.info("Initialize ModelHelper")

    @staticmethod
    def trello_cards(trello_cards):
        cards = []

        for trello_card in trello_cards:
            card = {
                "id": str(trello_card["_id"]),
                "name": trello_card["name"],
                "due": trello_card["due"],
                "url": trello_card["url"],
                "created_date": trello_card["created_date"]
            }

            cards.append(card)

        return cards
