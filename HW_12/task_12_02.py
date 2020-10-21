class Car:
    def __init__(self, make, model, year_of_manufacture, speed):
        self.__make = make
        self.__model = model
        self.__year_of_manufacture = year_of_manufacture
        self.__speed = speed

    def speed_increase(self):
        self.__speed += 5
        print(f'Автомобиль {self.__make} {self.__model} {self.__year_of_manufacture}'
              f' увеличил скорость на : {self.__speed} км.ч')
        return self.__make, self.__model, self.__year_of_manufacture, self.__speed

    def decrease_speed(self):
        self.__speed -= 5
        print(f'Автомобиль {self.__make} {self.__model} {self.__year_of_manufacture}'
              f' уменьшил скорость на : {self.__speed} км.ч')

    def stop(self):
        self.__speed = 0
        print(f'Автомобиль {self.__make} {self.__model} {self.__year_of_manufacture}'
              f' остановился его скорость = {self.__speed} км.ч')

    def reversed(self):
        self.__speed *= -1
        print(f'Значение скорости автомобиля изменилось на противоположное {self.__make} {self.__model} '
              f'{self.__year_of_manufacture} теперь оно = {self.__speed} км.ч')

    def printing_speed(self):
        print(f'Скорость автомобиля = {self.__speed} км.ч')

    def speed(self):
        return self.__speed


car = Car(make='BMW', model='3series', year_of_manufacture='2020', speed=0)
car.speed_increase()
car.decrease_speed()
car.printing_speed()
car.reversed()
car.stop()
