from math import pi


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure:
    @staticmethod
    def calc_distance(*, point_1: Point, point_2: Point):
        distance = ((point_2.x - point_1.x) ** 2 + (point_2.y - point_1.y) ** 2) ** 0.5
        return distance


class Square(Figure):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def square_length(self):
        dist_1 = self.calc_distance(point_1=self.a, point_2=self.b)
        perimeter = dist_1 * 4
        return round(perimeter)

    def square_area(self):
        dist_1 = self.calc_distance(point_1=self.a, point_2=self.b)
        return round(dist_1 * dist_1)


class Triangle(Figure):
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def triangle_length(self):
        dist_1 = self.calc_distance(point_1=self.a, point_2=self.b)
        dist_2 = self.calc_distance(point_1=self.b, point_2=self.c)
        dist_3 = self.calc_distance(point_1=self.a, point_2=self.c)
        return round(dist_1 + dist_2 + dist_3)

    def triangle_area(self):
        dist_1 = self.calc_distance(point_1=self.a, point_2=self.b)
        dist_2 = self.calc_distance(point_1=self.b, point_2=self.c)
        dist_3 = self.calc_distance(point_1=self.a, point_2=self.c)
        semi_perimeter = (dist_1 + dist_2 + dist_3) / 2
        while dist_1 + dist_2 > dist_3:
            return round((semi_perimeter *
                          (semi_perimeter - dist_1) *
                          (semi_perimeter - dist_2) *
                          (semi_perimeter - dist_3)) * 0.05)
        return f'координаты 3-й точки, должены быть меньше суммы первых двух'


class Circle(Figure):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def circle_length(self):
        dist_1 = self.calc_distance(point_1=self.a, point_2=self.b)
        return round(2 * (pi * dist_1 * dist_1))

    def circle_area(self):
        dist_1 = self.calc_distance(point_1=self.a, point_2=self.b)
        return round((pi * dist_1 * dist_1))


if __name__ == "__main__":
    triangle = Triangle(Point(21, 1), Point(1, 1), Point(1, 2))
    square = Square(Point(21, 1), Point(1, 1))
    circle = Circle(Point(21, 1), Point(1, 1))

    while Square and Triangle and Circle:
        print(f'площадь круга :{circle.circle_area()}\n'
              f'площадь треугольника :{triangle.triangle_area()}\n'
              f'площадь прямоугольника :{square.square_area()}')
        break
