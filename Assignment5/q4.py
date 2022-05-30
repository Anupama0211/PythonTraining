"""
Create a Point class with 2 arguments(x,y), and modify ‘str’ function to print in ‘(x,y)’ format.
Create 2 instances with different args lets say ob1 and ob2. Modify behaviour of ob1+ob2 to add the values of objects.

Example:
ob1 = Point(1,5)
ob2 = Point(2,7)

str(ob1) => ‘(1,5)’
ob3 = ob1+ob2
str(ob3) => ‘(3,12)’ , here x value from both objects are added, same for y

"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)


ob1 = Point(1, 5)
ob2 = Point(2, 7)
print("Point 1--", ob1)
print("Point 1--", ob2)
print(ob1 + ob2)
