from flask import request

from src.api import zac
from src.factories.factory_controller import FactoryController
from src.helpers.access_helper import required_token

factory = FactoryController()


@zac.route("/health", methods=["GET"])
def health():
    return {"message": "I'm OK!", "code": 200}


@zac.route("/api/tasks", methods=["GET"])
@required_token
def tasks(*args, **kwargs):
    user = kwargs.get("user")
    query = request.args.to_dict()

    factory_controller = FactoryController()
    task_controller = factory_controller.get_task()
    tasks = task_controller.get(user, query)

    return tasks


@zac.route("/api/tasks/<id>/conclude", methods=["POST"])
@required_token
def conclude(*args, **kwargs):
    id = kwargs.get("id")

    factory_controller = FactoryController()
    task_controller = factory_controller.get_task()
    tasks = task_controller.conclude(id)

    return {message: "Done"}
