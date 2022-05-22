"""
Create function to take arbitrary number of integer and return the average of those numbers
•	average(1,2,4,5,6) => 3.6
•	average(1,2,5,6) => 3.5
"""


def average(*nums) -> float:
    return sum(nums) / len(nums)


if __name__ == "__main__":
    print(average(1, 2, 4, 5, 6))
    print(average(1, 2, 5, 6))
