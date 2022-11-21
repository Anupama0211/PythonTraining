import datetime  # we will use this for date objects


class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        print("inittttttttttttttt")
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def __new__(cls, *args, **kwargs):
        print("newwwwwwwwwwwww")
        return super(Person, cls).__new__(cls)

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age


person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12),  # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(type(Person))
print(type(object))

print(person.name)
print(person.email)
print(person.age())


def outer():  # 1
    x = 5  # 2

    def inner():  # 3
        # nonlocal x
        print(x)  # 4
        # x += 1  # 5

        print(x)  # 6
    inner()

outer()  # 8


def outerFunction(text):
    def innerFunction():
        print(text)

    innerFunction()
print("OUTER FUNCTION TYPE ---",type(Person().email))

outer()
