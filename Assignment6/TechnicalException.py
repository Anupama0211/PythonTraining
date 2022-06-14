class TechnicalException(Exception):
    def __init__(self, message="Technical Error"):
        self.message = message
        super().__init__(self.message)
