"""
Write an algorithm that takes one or more filenames as arguments
and prints all the lines which are longer than 30 characters using generators.
"""


def generator(*filenames):
    for filename in filenames:
        with open(filename) as file:
            line = file.readline()
            if (len(line) > 30):
                yield line


for line in generator("file1.txt", "file2.txt"):
    print(line)