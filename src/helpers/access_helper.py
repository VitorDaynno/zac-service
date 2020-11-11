from src.helpers.jwt_helper import JWTHelper
from src.helpers.error_helper import Forbiden
from flask import request, make_response
from functools import wraps
from jwt import DecodeError


jwt_helper = JWTHelper()


def required_token(f):
    @wraps(f)
    def verify_token():
        headers = request.headers

        try:
            if "Authorization" not in headers:
                raise Forbiden("Bearer token must be provide")

            bearer_token = headers["Authorization"].split(" ")

            if len(bearer_token) < 2:
                raise Forbiden("Bearer token must be provide")

            token = bearer_token[1]

            user = jwt_helper.decode_token(token)

            return f()
        except Forbiden as error:
            code = error.code
            message = error.message
            error = {"message": message}
            response = make_response(error, code)
            return response
        except DecodeError:
            code = 403
            message = "Invalid token"
            error = {"message": message}
            response = make_response(error, code)
            return response

    return verify_token
