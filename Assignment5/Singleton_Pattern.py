""" Singleton Design Pattern"""


class Singleton():
    __instance = None

    def __init__(self, name):
        self.name = name

    def __new__(cls, name):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


name1 = Singleton("Python")
print(id(name1))
print(name1.name)
name2 = Singleton("Python3")
print(id(name2))
print(name1.name)
