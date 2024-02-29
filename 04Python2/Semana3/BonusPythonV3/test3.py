class CustomException(Exception):
    description = None
    id = None

    def __init__(self):
        super().__init__(f'{self.description}: {self.id}')