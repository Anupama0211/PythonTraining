class NoOrdersSubmittedException(Exception):
    def __init__(self, message="WARNING: User have no submitted orders."):
        self.message = message
        super().__init__(self.message)
