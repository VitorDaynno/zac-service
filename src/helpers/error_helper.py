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

class NotFound(Exception):
    def __init__(self, message):
        super()
        self.code = 404
        self.message = message

class Conflict(Exception):
    def __init__(self, message):
        super()
        self.code = 409
        self.message = message

class UnprocessableEntity(Exception):
    def __init__(self, message):
        super()
        self.code = 422
        self.message = message
