class Service:
    data = []

    def __init__(self, name):
        self.name = name


obj = Service("Sanchit")

print(obj.name)
print(obj.data)
obj.data.append(1)
print(obj.data)

obj1 = Service("Santosh")
print(obj1.data)
obj1.data.append(2)
print(obj1.data)