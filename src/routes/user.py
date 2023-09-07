from flask import request, make_response

from src.api import zac
from src.config.logger import logger
from src.factories.factory_controller import FactoryController
from src.helpers.error_helper import Unauthorized, UnprocessableEntity


factory = FactoryController()


@zac.route("/users/auth", methods=["POST"])
def auth():
    try:
        body = request.json or {}

        if "email" not in body or "password" not in body:
            raise UnprocessableEntity("Email or password is required")

        email = body["email"]
        password = body["password"]

        logger.info("Initializing auth user")
        user = factory.get_user()
        token = user.auth(email, password)

        return token
    except (Unauthorized, UnprocessableEntity) as error:
        code = error.code
        message = error.message
        error = {"message": message}
        response = make_response(error, code)
        return response
    except Exception as error:
        error = {"error": str(error)}
        response = make_response(error, 500)
        return response
