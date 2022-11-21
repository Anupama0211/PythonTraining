"""
Create a custom exception class which takes a string message as attribute
"""


class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def check_age(age):
    if age < 18:
        raise CustomException("Age is not valid")
    print("Age is Valid")


try:
    check_age(19)
    check_age(12)
except CustomException as e:
    print(e)
