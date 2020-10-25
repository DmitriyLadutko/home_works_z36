class Dog:
    def __init__(self, name, age, master=None):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'собачка {self.name} бежит')

    def jump(self):
        print(f'собачка {self.name} прыгает')

    def birthday(self):
        print(f'у собачки {self.name} День Рождения ей исполнилось {self.age + 1} лет')

    def sleep(self):
        print(f'собачки {self.name} спит')

    def bark(self):
        print(f'собачка {self.name} лаит')


dog = Dog(name='Joe', age=12)

dog.run()
dog.jump()
dog.birthday()
dog.sleep()
dog.bark()


class Cat:
    def __init__(self, name, age, master=None):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'котик {self.name} бежит')

    def jump(self):
        print(f'котик {self.name} - прыгает')

    def birthday(self):
        print(f'у котика {self.name} День Рождения ему исполнилось {self.age + 1} лет')

    def sleep(self):
        print(f'котик {self.name} спит')

    def meow(self):
        print(f'котик {self.name} мяучит')


cat = Cat(name='Kiki', age=4)

cat.run()
cat.jump()
cat.birthday()
cat.sleep()
cat.meow()


class Parrot:
    def __init__(self, name, age, master=None):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        print(f'попугай {self.name} бежит')

    def jump(self):
        print(f'попугай {self.name} прыгает')

    def birthday(self):
        print(f'у попугая {self.name} День Рождения ему исполнилось {self.age + 1} лет')

    def sleep(self):
        print(f'попугай {self.name} спит')

    def fly(self):
        print(f'попугай {self.name} летает')


parrot = Parrot(name='Kesha', age=4,)
parrot.run()
parrot.jump()
parrot.birthday()
parrot.fly()
