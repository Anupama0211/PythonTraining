"""
Create function to take arbitrary number of integer and return the average of those numbers
•	average(1,2,4,5,6) => 3.6
•	average(1,2,5,6) => 3.5
"""


def average(*nums) -> float:
    return sum(nums) / len(nums)


if __name__ == "__main__":
    try:
        print(average())
    except ZeroDivisionError:
        print("Division by Zero is not allowed")
    try:
        print(average(1, 2, 5, 6))
    except ZeroDivisionError as e:
        print("Division by Zero is not allowed")
