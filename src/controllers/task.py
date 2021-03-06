from src.config.logger import logger
from src.helpers.error_helper import NotFound, Conflict

import json

class Task:
    def __init__(self, trello_card_controller, zac_task_controller, routine_controller, model_helper):
        logger.info("Initializing Tasks")
        self._trello_card_controller = trello_card_controller
        self._zac_task_controller = zac_task_controller
        self._routine_controller = routine_controller
        self._model_helper = model_helper

    def get(self, user, query):
        logger.info("Initializing get tasks")

        trello_user = user["trello_user"]
        telegram_user = user["telegram_user"]

        trello_query = query
        trello_query["user"] = trello_user
        trello_cards = self._trello_card_controller.get(trello_query)

        is_conclude = query.is_conclude if "is_conclude" in query else False
        is_failed = query.is_failed if "is_failed" in query else False

        zac_query = query
        zac_query["user"] = telegram_user
        zac_query["isConclude"] = is_conclude
        zac_query["is_failed"] = is_failed

        zac_tasks = self._zac_task_controller.get(zac_query)

        cards = self._model_helper.trello_cards(trello_cards)
        tasks = self._model_helper.zac_tasks(zac_tasks)

        tasks.extend(cards)
        tasks.sort(key=lambda x: x.get("date") or x.get("due"))

        return {"tasks": tasks}

    def get_scheduled(self, user, query):
        logger.info("Initializing get scheduled tasks")

        trello_user = user["trello_user"]
        telegram_user = user["telegram_user"]

        trello_query = query
        trello_query["user"] = trello_user
        trello_cards = self._trello_card_controller.get(trello_query)

        is_conclude = query.is_conclude if "is_conclude" in query else False
        is_failed = query.is_failed if "is_failed" in query else False

        zac_query = query
        zac_query["user"] = telegram_user
        # zac_query["isConclude"] = is_conclude
        # zac_query["is_failed"] = is_failed

        zac_tasks = self._zac_task_controller.get(zac_query)

        is_active = query.is_active if "is_active" in query else True

        routine_query = query
        routine_query["user"] = telegram_user
        routine_query["days"] = json.loads(query["days"])
        routine_query["isActive"] = is_active

        zac_routines = self._routine_controller.get(routine_query)

        cards = self._model_helper.trello_cards(trello_cards)
        tasks = self._model_helper.zac_tasks(zac_tasks)
        routines = self._model_helper.zac_routines(zac_routines)

        tasks.extend(cards)
        tasks.sort(key=lambda x: x.get("date") or x.get("due"))

        return {"tasks": tasks, "routines": routines}

    def conclude(self, user, id):
        logger.info("Initializing conclude task")

        telegram_user = user["telegram_user"]

        filter = { "id": id, "user": telegram_user }

        tasks = self._zac_task_controller.get(filter)

        if len(tasks) == 0:
            logger.error("Task not found")
            raise NotFound("Task not found")

        task = tasks[0]
        if task["isConclude"] or ("is_failed" in task and task["is_failed"]):
            logger.error("Task is already concluded or failed")
            raise Conflict("Task is already concluded or failed")

        self._zac_task_controller.update(filter, {"isConclude": True})

    def fail(self, user, id):
        logger.info("Initializing fail task")

        telegram_user = user["telegram_user"]

        filter = { "id": id, "user": telegram_user }

        tasks = self._zac_task_controller.get(filter)

        if len(tasks) == 0:
            logger.error("Task not found")
            raise NotFound("Task not found")

        task = tasks[0]
        if task["isConclude"] or ("is_failed" in task and task["is_failed"]):
            logger.error("Task is already concluded or failed")
            raise Conflict("Task is already concluded or failed")

        self._zac_task_controller.update(filter, {"is_failed": True})