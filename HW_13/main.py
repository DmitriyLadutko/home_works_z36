from classes import *

point = Point(x=0, y=0)
circle = Circle(10, None, None, None)
triangle = Triangle(6, 7, 12)
square = Square(5, 2, 2)
point.point_description()
circle.circle_length()
circle.circle_area()
triangle.triangle_area()
triangle.triangle_length()
square.square_area()
square.square_length()

all_func = Square, Triangle, Circle
while all_func:
    print(f'площадь круга {circle.circle_area()}\n'
          f'площадь триугольника {triangle.triangle_area()}\n'
          f'площадь прямоугольника {square.square_area()}')
    break
