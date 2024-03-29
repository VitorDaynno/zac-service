from flask import request, make_response
from bson.errors import InvalidId

from src.api import zac
from src.factories.factory_controller import FactoryController
from src.helpers.access_helper import required_token
from src.helpers.error_helper import NotFound, Conflict

factory = FactoryController()


@zac.route("/health", methods=["GET"])
def health():
    return {"message": "I'm OK!", "code": 200}

@zac.route("/tasks", methods=["GET"])
@required_token
def tasks(*args, **kwargs):
    user = kwargs.get("user")
    query = request.args.to_dict()

    factory_controller = FactoryController()
    task_controller = factory_controller.get_task()
    tasks = task_controller.get(user, query)

    return tasks

@zac.route("/tasks", methods=["POST"])
@required_token
def create_task(*args, **kwargs):
    user = kwargs.get("user")
    body = request.json or {}

    factory_controller = FactoryController()
    task_controller = factory_controller.get_task()
    task = task_controller.create(user, body)

    return task

@zac.route("/tasks/<id>", methods=["PUT"])
@required_token
def update_task(*args, **kwargs):
    try:
        id = kwargs.get("id")
        body = request.json or {}

        user = kwargs.get("user")

        factory_controller = FactoryController()
        task_controller = factory_controller.get_task()
        task = task_controller.update(user, id, body)

        return task
    except (NotFound, Conflict) as error:
        code = error.code
        message = error.message
        error = {"message": message}
        response = make_response(error, code)
        return response
    except InvalidId as error:
        error = {"message": "Invalid id"}
        response = make_response(error, 422)
        return response
    except Exception as error:
        error = {"error": str(error)}
        response = make_response(error, 500)
        return response

@zac.route("/api/scheduled-tasks", methods=["GET"])
@required_token
def schedules_tasks(*args, **kwargs):
    try:
        user = kwargs.get("user")
        query = request.args.to_dict()

        factory_controller = FactoryController()
        task_controller = factory_controller.get_task()
        tasks = task_controller.get_scheduled(user, query)

        return tasks
    except Exception as error:
        error = {"error": str(error)}
        response = make_response(error, 500)
        return response

@zac.route("/tasks/<id>/conclude", methods=["POST"])
@required_token
def conclude(*args, **kwargs):
    try:
        id = kwargs.get("id")
        user = kwargs.get("user")

        factory_controller = FactoryController()
        task_controller = factory_controller.get_task()
        tasks = task_controller.conclude(user, id)

        return {"message": "Done"}
    except (NotFound, Conflict) as error:
        code = error.code
        message = error.message
        error = {"message": message}
        response = make_response(error, code)
        return response
    except InvalidId as error:
        error = {"message": "Invalid id"}
        response = make_response(error, 422)
        return response
    except Exception as error:
        error = {"error": str(error)}
        response = make_response(error, 500)
        return response

@zac.route("/tasks/<id>/fail", methods=["POST"])
@required_token
def fail(*args, **kwargs):
    try:
        id = kwargs.get("id")
        user = kwargs.get("user")

        factory_controller = FactoryController()
        task_controller = factory_controller.get_task()
        tasks = task_controller.fail(user, id)

        return {"message": "Done"}
    except (NotFound, Conflict) as error:
        code = error.code
        message = error.message
        error = {"message": message}
        response = make_response(error, code)
        return response
    except InvalidId as error:
        error = {"message": "Invalid id"}
        response = make_response(error, 422)
        return response
    except Exception as error:
        error = {"error": str(error)}
        response = make_response(error, 500)
        return response

@zac.route("/tasks/<id>", methods=["DELETE"])
@required_token
def delete(*args, **kwargs):
    try:
        id = kwargs.get("id")
        user = kwargs.get("user")

        factory_controller = FactoryController()
        task_controller = factory_controller.get_task()
        task_controller.delete(user, id)

        return {"message": "Done"}
    except (NotFound, Conflict) as error:
        code = error.code
        message = error.message
        error = {"message": message}
        response = make_response(error, code)
        return response
    except InvalidId as error:
        error = {"message": "Invalid id"}
        response = make_response(error, 422)
        return response
    except Exception as error:
        error = {"error": str(error)}
        response = make_response(error, 500)
        return response