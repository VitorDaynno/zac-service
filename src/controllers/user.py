from src.config.logger import logger
from src.helpers.error_helper import Unauthorized, NotFound


class User:
    def __init__(self, dao, date_helper, crypto_helper, model_helper, jwt_helper):
        logger.info("Initializing user")
        self._dao = dao
        self._date_helper = date_helper
        self._crypto_helper = crypto_helper
        self._model_helper = model_helper
        self._jwt_helper = jwt_helper

    def auth(self, email, password):
        logger.info("Initializing auth")

        encrypted_password = self._crypto_helper.to_sha256(password)

        users = self._dao.get({"email": email, "password": encrypted_password})

        if len(users) == 0:
            raise Unauthorized("Email or password is incorrect")

        user = self._model_helper.user(users[0])

        token = self._jwt_helper.encode_token(user)

        user["token"] = token

        return {
            "id": user["id"],
            "email": user["email"],
            "token": token
        }

    def get(self, filters):
        logger.info("Initializing get users")
        cards = self._dao.get(filters)
        return cards

    def get_by_id(self, id):
        logger.info("Initializing get by id")
        users = self._dao.get({ "id": id })

        if not len(users):
            raise NotFound('User not found')

        return users[0]