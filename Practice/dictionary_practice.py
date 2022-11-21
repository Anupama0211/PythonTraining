# tuple_1 = (22, 33, [33, 22])
# print(type(tuple_1))
# dict11 = {}
# dict11[tuple_1] = 3
# print(dict11)
from collections import Counter, namedtuple


class A():
    pass


print("-----", isinstance(A, object))
print(type(A))
print(type(object))
a=[1,2,3,3,3,3,3,1,1,2,2]
c=Counter(a)
for i in c:
    print(i)
print(c)
namedtuple
# dict0={"s":2,2:2,3:222}
# i=iter(dict0)
# for h in i:
#     print(h)