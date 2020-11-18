from src.config.logger import logger


class Task:
    def __init__(self, trello_card_controller, zac_task_controller, model_helper):
        logger.info("Initializing Tasks")
        self._trello_card_controller = trello_card_controller
        self._zac_task_controller = zac_task_controller
        self._model_helper = model_helper

    def get(self, user, query):
        logger.info("Initializing get tasks")

        trello_user = user["trello_user"]
        telegram_user = user["telegram_user"]

        trello_query = query
        trello_query["user"] = trello_user
        trello_cards = self._trello_card_controller.get(trello_query)

        is_conclude = query.is_conclude if "is_conclude" in query else False

        zac_query = query
        zac_query["user"] = telegram_user
        zac_query["isConclude"] = is_conclude

        zac_tasks = self._zac_task_controller.get(zac_query)

        cards = self._model_helper.trello_cards(trello_cards)
        tasks = self._model_helper.zac_tasks(zac_tasks)

        tasks.extend(cards)
        tasks.sort(key=lambda x: x.get("date") or x.get("due"))

        return {"tasks": tasks}

    def conclude(self, user, id):
        logger.info("Initializing conclude task")

        telegram_user = user["telegram_user"]
