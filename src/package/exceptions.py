class MyAppValueError(ValueError):
    def __init__(self, message, *args):         
        super(MyAppValueError, self).__init__(message, *args)

