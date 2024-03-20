# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
print("create a namedtuple type, Point, with fields x and y")
print("...like creating a light-weight class")
print(" namedtuples help keep track of things as they get more complex")
Point = collections.namedtuple("Point", "x y")
print("create a couple of namedtuple variables, p1, p2\n\n")
p1 = Point(10, 20)
p2 = Point(30, 40)
print(p1, p2)
print(p1.x, p1.y, p2.x, p2.y, "\n")

# TODO: use _replace to create a new instance
print("to modify a namedtuple, use the _replace method")
print('p1 = p1._replace(x = 100)')
p1 = p1._replace(x = 100)
print(p1, "\n")