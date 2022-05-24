def deco(num):
    def inner_deco(func):
        def inner(value):
            func(value)

        return inner

    return inner_deco


@deco(10)
def caller(a):
    print('Caller', a)


caller(20)
