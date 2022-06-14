"""
. Create a custom context manager class for file handling?
"""


class open_file:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with open("file1.txt", 'w') as file:
    file.write("ASSIGNMENT 6 QUESTION 1")

print(file.closed)  # True
