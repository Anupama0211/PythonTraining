import sys


def decorator_factory(a):
    print("Inside Decorator Factory1")

    def decorator_function(func):
        print("Inside Derocator Function1")

        def wrapper_function(*args, **kwargs):
            print("Inside Derocator Function")
            print(f"before____{args}{a}")
            print(f"before_____{kwargs}{a}")
            result = func(*args, **kwargs)
            print(f"after___{a}")
            return result

        print("Inside Derocator Function2")
        return wrapper_function

    print("Inside Decorator Factory2")
    return decorator_function

#
# @decorator_factory(5)
# def display(name, age):
#     print(f"Name -{name}\n Age--{age}")


# print("OUTSIDE")
#
# display("Anupama", 23)
# display("Anup", 23)

if __name__ == "__main__":
#     # code for testing decorator chaining
#     def decor2(func):
#         def inner():
#             print("hi..2")
#             func()
#
#         return inner
# # decor1(decor2(num))
#
#     def decor1(func):
#         def inner():
#             print("hi..1")
#             func()
#
#         return inner
#
#
#     @decor1
#     @decor2
#     def num():
#         print("How are you", 10)

    # num()
    square=(x+x for x in range(10))
    print(type(square))
    print(sys.getsizeof(square))
    print(sys.getsizeof(list(square)))
    # gen =square()
    print(next(square))
    print(next(square))