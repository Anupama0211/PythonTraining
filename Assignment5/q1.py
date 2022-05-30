"""
Create a class with public, private and protected methods, create 2 instances and compare if ‘id’ of instances are same . Create a class with public, private and protected
methods, create 2 instances and compare if ‘id’ of instances are same
"""


class Demo:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def public_method(self):
        print("public method")

    def _protected_method(self):
        print("protected method")

    def __private_method(self):
        print("private method")


obj1 = Demo(1, 2)
obj2 = Demo(3, 4)

print(id(obj1) == id(obj2))
