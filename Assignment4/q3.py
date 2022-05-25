"""
Write an algorithm that takes one or more filenames as arguments
and prints all the lines which are longer than 30 characters using generators.
"""


def generator(filenames):
    for filename in filenames:
        if filename > 30:
            yield filename

