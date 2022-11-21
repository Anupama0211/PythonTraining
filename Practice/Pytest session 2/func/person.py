class Person:
    def __init__(self, name, age, credit):
        self.name = name
        self.age = age
        self.credit = credit
    
    def get_age(self):
        return self.age
    
    def get_credit(self):
        return self.credit
    
    def add_credit(self, value):
        self.credit += value
        return self.credit
    


def is_eligible(person):
    return person.get_age() >= 18