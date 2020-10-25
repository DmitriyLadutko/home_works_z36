from math import pi


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def point_description(self):
        if self.x == 0 and self.y == 0:
            return f'Начало координат'
        elif self.x > 0 and self.y > 0:
            return f'Точка находится в I четверти'
        elif self.x < 0 and self.y > 0:
            return f'Точка находится вo II четверти'
        elif self.x < 0 and self.y < 0:
            return f'Точка находится в III четверти'
        return f'Точка находится в IV четверти'


class Figure:
    def __init__(self, *args):
        self.point_1, self.point_2, self.point_3 = args


class Circle(Figure):
    def __init__(self, radius, *args):
        super(Circle, self).__init__(*args)
        self.radius = radius

    def circle_length(self):
        return round((2 * pi * self.radius), 2)

    def circle_area(self):
        return round((pi * self.radius * self.radius), 2)


class Triangle(Figure):
    def __init__(self, *args):
        super(Triangle, self).__init__(*args)

    def triangle_area(self):
        semi_perimeter = (self.point_1 + self.point_2 + self.point_3) / 2
        while self.point_1 + self.point_2 > self.point_3:
            return round(((semi_perimeter * (semi_perimeter - self.point_1) *
                           (semi_perimeter - self.point_2) *
                           (semi_perimeter - self.point_3)) ** 0.5), 2)
        return f'Введенный 3-й аргумент, должен быть меньше суммы первых двух'

    def triangle_length(self):
        return round((self.point_1 + self.point_2 + self.point_3), 2)


class Square(Figure):
    def __init__(self, *args):
        super(Square, self).__init__(*args)

    def square_area(self):
        return round((self.point_1 * self.point_2), 2)

    def square_length(self):
        return round((2 * (self.point_1 * self.point_2)), 2)


if __name__ == '__main__':
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
