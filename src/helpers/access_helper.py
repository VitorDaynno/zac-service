from src.helpers.jwt_helper import JWTHelper
from src.helpers.error_helper import Forbiden
from flask import request, make_response, abort
from functools import wraps
from jwt import DecodeError, ExpiredSignatureError


jwt_helper = JWTHelper()


def required_token(f):
    @wraps(f)
    def verify_token(*args, **kwargs):
        headers = request.headers

        try:
            if "Authorization" not in headers:
                raise Forbiden("Bearer token must be provide")

            bearer_token = headers["Authorization"].split(" ")

            if len(bearer_token) < 2:
                raise Forbiden("Bearer token must be provide")

            token = bearer_token[1]

            user = jwt_helper.decode_token(token)
            kwargs["user"] = user
            return f(*args, **kwargs)
        except Forbiden as error:
            code = error.code
            message = error.message
            error = {"message": message}
            response = make_response(error, code)
            response.content_type = "application/json"
            abort(response)
        except (DecodeError, ExpiredSignatureError) as error:
            code = 403
            message = "Invalid token"
            error = {"message": message}
            response = make_response(error, code)
            response.content_type = "application/json"
            abort(403)

    return verify_token
