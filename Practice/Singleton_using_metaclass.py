# class Singleton(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__new__(*args, **kwargs)
#         return cls._instances[cls]

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args,**kwargs)
        return cls._instances[cls]


class MyClass(metaclass=Singleton):
    pass


obj1 = MyClass()
obj2 = MyClass()

print(obj2 is obj1)

