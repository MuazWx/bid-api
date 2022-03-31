class RequestBodyException(BaseException):
    def __init__(self):
        super().__init__('Malformed request body')
