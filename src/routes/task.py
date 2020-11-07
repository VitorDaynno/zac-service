from flask import request, jsonify
import json

from src.api import zac
from src.factories.factory_controller import FactoryController

factory = FactoryController()


@zac.route("/health", methods=["GET"])
def health():
    return {"message": "I'm OK!", "code": 200}


@zac.route("/api/tasks", methods=["GET"])
def tasks():
    query = request.args.to_dict()

    factory_controller = FactoryController()
    task_controller = factory_controller.get_task()
    tasks = task_controller.get(query)

    return tasks
