import random
import numpy


class Matrix:
    m, n = None, None
    data = [[]]

    def __init__(self, *, n=5, m=5, a=0, b=0):
        self.n = n
        self.m = m
        self.a = a
        self.b = b
        Matrix.n, m = n, m
        Matrix.data = numpy.array([[random.randint(a, b) for _ in range(n)] for _ in range(m)])

    def __str__(self):
        return f' {Matrix.data}'

    @classmethod
    def find_max(cls):
        return f'{numpy.amax(Matrix.data)} - max element in matrix'

    @classmethod
    def find_min(cls):
        return f'{numpy.amin(Matrix.data)} - min element in matrix'

    @classmethod
    def find_sum(cls):
        return f'{numpy.sum(Matrix.data)} sum all elements in matrix'


if __name__ == '__main__':
    matrix = Matrix()
    print(matrix)
    print(matrix.find_max())
    print(matrix.find_min())
    print(matrix.find_sum())
