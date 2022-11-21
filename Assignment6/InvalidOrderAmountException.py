class InvalidOrderAmountException(Exception):
    def __init__(self, message="ERROR: Wrong order amount."):
        self.message = message
        super().__init__(self.message)
