from classes import *

triangle = Triangle(Point(21, 1), Point(1, 1), Point(1, 2))
square = Square(Point(21, 1), Point(1, 1))
circle = Circle(Point(21, 1), Point(1, 1))

while Square and Triangle and Circle:
    print(f'площадь круга {circle.circle_area()}\n'
          f'площадь треугольника {triangle.triangle_area()}\n'
          f'площадь прямоугольника {square.square_area()}')
    break
