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

    @staticmethod
    def user(user):
        user_entity = {
            "id": str(user["_id"]),
            "email": user["email"],
            "trello_user": user["trello_user"] if "trello_user" in user else "",
            "telegram_user": user["telegram_user"]
            if "telegram_user" in user else ""
        }

        return user_entity

    @staticmethod
    def zac_tasks(zac_tasks):
        tasks = []

        for zac_task in zac_tasks:
            task = {
                "id": str(zac_task["_id"]),
                "name": zac_task["name"],
                "due": zac_task["date"]
            }

            tasks.append(task)

        return tasks
