"""
We have a division method which throws exception when we divide a number by zero.
We need to write a class-based decorator which works as exception handler for division method.
"""


class Decorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, number1, number2):
        try:
            return self.function(number1, number2)
        except ZeroDivisionError as e:
            return e


@Decorator
def division(number1, number2):
    return number1 / number2


print(division(7, 8))
print(division(7, 0))
