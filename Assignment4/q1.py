"""
Create a generator-based method to print even numbers from 0 to 50.
"""


def even_nums_generator():
    i = 0
    while i <= 50:
        yield i
        i += 2


gen_obj = even_nums_generator()
for i in gen_obj:
    print(i)
