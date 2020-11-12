class Unauthorized(Exception):
    def __init__(self, message):
        super()
        self.code = 401
        self.message = message


class Forbiden(Exception):
    def __init__(self, message):
        super()
        self.code = 403
        self.message = message


class UnprocessableEntity(Exception):
    def __init__(self, message):
        super()
        self.code = 422
        self.message = message
