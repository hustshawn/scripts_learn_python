from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

print(isinstance(p, Point))
print(isinstance(p, tuple))

# To define an circle, namedtuple can be used
Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle = Circle(5, 6, 10)
print(circle.x, circle.y, circle.r)
