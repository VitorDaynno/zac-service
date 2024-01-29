from flask import request, make_response, abort
from bson.errors import InvalidId

from src.api import zac
from src.factories.factory_controller import FactoryController
from src.helpers.access_helper import required_token
from src.helpers.error_helper import NotFound, Conflict

factory = FactoryController()


@zac.route("/routines", methods=["POST"])
@required_token
def create_routine(*args, **kwargs):
    try:
        user = kwargs.get("user")
        body = request.json or {}

        factory_controller = FactoryController()
        routine_controller = factory_controller.get_routine()
        routine = routine_controller.create(user, body)

        return make_response(routine, 201)
    except Exception as error:
        code = error.code
        message = error.message
        error = {"message": message}
        response = make_response(error, code)
        response.content_type = "application/json"
        abort(response)