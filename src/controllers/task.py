from src.config.logger import logger
from src.helpers.error_helper import NotFound, Conflict, UnprocessableEntity

import json

class Task:
    def __init__(
            self,
            trello_card_controller,
            zac_task_controller,
            routine_controller,
            user_controller,
            model_helper,
            date_helper
        ):
        logger.info("Initializing Tasks")
        self._trello_card_controller = trello_card_controller
        self._zac_task_controller = zac_task_controller
        self._routine_controller = routine_controller
        self._user_controller = user_controller
        self._model_helper = model_helper
        self._date_helper = date_helper

    def get(self, user, query):
        logger.info("Initializing get tasks")

        trello_user = user["trello_user"]

        trello_query = query
        trello_query["user"] = trello_user
        trello_cards = self._trello_card_controller.get(trello_query)

        zac_query = query
        zac_query["user"] = user["id"]

        zac_tasks = self._zac_task_controller.get(zac_query)

        cards = self._model_helper.trello_cards(trello_cards)
        tasks = self._model_helper.zac_tasks(zac_tasks)

        tasks.extend(cards)
        tasks.sort(key=lambda x: x.get("date") or x.get("due"))

        return { "tasks": tasks }

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

        filter = { "id": id, "user": user["id"] }

        tasks = self._zac_task_controller.get(filter)

        if len(tasks) == 0:
            logger.error("Task not found")
            raise NotFound("Task not found")

        task = tasks[0]
        if task["is_conclude"] or ("is_failed" in task and task["is_failed"]):
            logger.error("Task is already concluded or failed")
            raise Conflict("Task is already concluded or failed")

        self._zac_task_controller.update(filter, {"is_conclude": True})

    def fail(self, user, id):
        logger.info("Initializing fail task")

        filter = { "id": id, "user": user["id"] }

        tasks = self._zac_task_controller.get(filter)

        if len(tasks) == 0:
            logger.error("Task not found")
            raise NotFound("Task not found")

        task = tasks[0]
        if task["is_conclude"] or ("is_failed" in task and task["is_failed"]):
            logger.error("Task is already concluded or failed")
            raise Conflict("Task is already concluded or failed")

        self._zac_task_controller.update(filter, {"is_failed": True})

    def create(self, user, body):
        task = self._zac_task_controller.create(user, body)

        return self._model_helper.zac_tasks(task)[0]

    def update(self, user, id, body):
        logger.info("Initializing update task")

        filter = { "id": id, "user": user["id"] }

        tasks = self._zac_task_controller.get(filter)

        if len(tasks) == 0:
            logger.error("Task not found")
            raise NotFound("Task not found")

        task = self._zac_task_controller.update(filter, body)

        return self._model_helper.zac_tasks(task)[0]

    def verify_task(self, task):
        if not task.name:
            raise UnprocessableEntity("Name is required")

    def delete(self, user, id):
        logger.info("Initializing delete task")

        filter = { "id": id, "user": user["id"] }

        tasks = self._zac_task_controller.get(filter)

        if len(tasks) == 0:
            logger.error("Task not found")
            raise NotFound("Task not found")

        self._zac_task_controller.update(filter, {"is_enabled": False})

    def create_tasks_by_routine(self):
        logger.info("Starting creating tasks by routines")

        routines = self._routine_controller.get_pending_routines()

        for routine in routines:
            try:
                user = self._user_controller.get_by_id(routine["user_id"])

                now = self._date_helper.now()
                day_of_week = self._date_helper.get_week_day(now, user["timezone"])

                local_date = self._date_helper.to_local_date(str(now), user["timezone"])
                parsed_date = self._date_helper.to_str_date(now, "%Y-%m-%d")
                parsed_timezone = self._date_helper.timezone_to_hour(user["timezone"])

                if day_of_week in routine["days"]:
                    routine_id = routine["_id"]
                    task = {
                        "name": routine["name"],
                        "date": str(local_date),
                        "startTime": parsed_date + " " + routine["start_time"] + " " + parsed_timezone,
                        "endTime": parsed_date + " " + routine["end_time"] + " " + parsed_timezone,
                        "user_id": routine["user_id"],
                        "note": ""
                    }

                    self.create({ "id": routine["user_id"]}, task)

                    self._routine_controller.update_last_created_date(routine_id, now)
            except Exception as error:
                logger.info("An error occurred: {0}".format(error))
