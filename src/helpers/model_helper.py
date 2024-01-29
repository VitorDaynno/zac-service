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
                "created_date": trello_card["created_date"],
                "duration": trello_card["duration"] if "duration" in trello_card else 25
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
                "startTime": zac_task["start_time"],
                "date": zac_task["date"],
                "endTime": zac_task["end_time"],
                "duration": zac_task["duration"] if "duration" in zac_task else 25,
                "note": zac_task["note"] if "note" in zac_task else None,
                "isConclude": zac_task["is_conclude"] if "is_conclude" in zac_task else False,
                "isFailed": zac_task["is_failed"] if "is_failed" in zac_task else False
            }

            tasks.append(task)

        return tasks

    @staticmethod
    def zac_routines(zac_routines):
        routines = []

        for zac_routine in zac_routines:
            routine = {
                "id": str(zac_routine["_id"]),
                "name": zac_routine["name"],
                "startTime": zac_routine["start_time"],
                "endTime": zac_routine["end_time"],
                "duration": zac_routine["duration"] if "duration" in zac_routine else 25
            }

            routines.append(routine)

        return routines
