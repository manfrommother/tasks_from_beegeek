'''
Shape
-Circle
-Polygon
--Quadrilateral
---Parallelogtam
---Rectangle
---Square
--Triangle
---IsoscelesTriangle
---EquilateralTriangle
'''
class Shape:
    pass

class Circle(Shape):
    pass

class Polygon(Shape):
    pass
class Quadrilateral(Polygon):
    pass
class Parallelogtam(Quadrilateral):
    pass
class Rectangle(Quadrilateral):
    pass
class Square(Quadrilateral):
    pass

class Triangle(Polygon):
    pass
class IsoscelesTriangle(Triangle):
    pass
class EquilateralTriangle(Triangle):
    pass


print(issubclass(Triangle, Polygon))
print(issubclass(IsoscelesTriangle, Triangle))
print(issubclass(EquilateralTriangle, Triangle))