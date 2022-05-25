"""
Create a generator-based method to print even numbers from 0 to 50.
"""


def even_nums_generator():
    i = 0
    while i <= 50:
        yield i
        i += 2


for even_num in even_nums_generator():
    print(even_num)
