class Employee:

    def __init__(self):
        print('This message is from Employee')


class Department:

    def __init__(self):
        print('This Department is inherited from Employee')


class Sales(Employee, Department):
    def jj(self):
        super().__init__()


if __name__ == "__main__":
    print(Sales())
    a = set('abracadabra')
    print(a)
    print(a)
    ran = range(4)
    print(ran)
    print(list(map(lambda x: x + 2, ran)))
    strin="Anupama"
    print("".join(reversed(strin)))
    sorted()