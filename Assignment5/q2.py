"""
Create class that can count no. of instances created using the class
"""


class CountInstances:
    count = 0

    def __init__(self):
        CountInstances.count += 1


obj1 = CountInstances()
obj2 = CountInstances()
obj2 = CountInstances()

print(CountInstances.count)
