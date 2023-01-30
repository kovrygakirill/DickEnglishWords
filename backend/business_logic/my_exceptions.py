class ProblemWithDataBase(Exception):
    def __init__(self, message: str = "DataBase had some problems"):
        self.message = message


class ProblemWithGenerateToken(Exception):
    def __init__(self, message: str = "Cannot generate token!"):
        self.message = message
