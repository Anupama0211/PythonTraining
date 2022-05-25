"""
We have a division method which throws exception when we divide a number by zero.
We need to write a class-based decorator which works as exception handler for division method.
"""


class Decorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, number1, number2):
        try:
            print(self.function(number1, number2))
        except ZeroDivisionError as e:
            print("Division by 0 is not allowed")


@Decorator
def division(number1, number2):
    return number1 / number2


division(7, 8)
division(7, 0)
