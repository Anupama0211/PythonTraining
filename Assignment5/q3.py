"""
Create class method, static method and instance method in a class
"""


class Mehtods:
    def instance_method(self):
        print("Instance Method")

    @classmethod
    def class_method(cls):
        print("Class Method")

    @staticmethod
    def static_method():
        print("Static Method")


obj = Mehtods()
obj.instance_method()
Mehtods.class_method()
Mehtods.static_method()
