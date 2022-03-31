class WrongTimeException(BaseException):
    def __init__(self):
        self.message = 'Wrong datetime specified'
