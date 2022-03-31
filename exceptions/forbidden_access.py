class ForbiddenAccess(BaseException):
    def __init__(self):
        super().__init__('Unauthorized access')
