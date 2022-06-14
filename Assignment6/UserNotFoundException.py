class UserNotFoundException(Exception):
    def __init__(self, message="WARNING: User ID doesn't exist."):
        self.message = message
        super().__init__(self.message)
