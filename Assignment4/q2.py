"""
Write a function my_enumerate that works like enumerate.
"""


def my_enumerate(iterable, start=0):
    for i in iterable:
        yield start, i
        start += 1


nums = [22, 332, 112]
for enu in my_enumerate(nums):
    print(enu)
