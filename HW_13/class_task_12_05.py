class MyTime:
    def __init__(self, *args):
        self.hours, self.minutes, self.seconds = self.get_values(args)

    @staticmethod
    def get_values(args):
        len_args = len(args)
        if len_args == 3:
            return args

        elif len_args == 1 and isinstance(args[0], str):
            if len(args[0].split(':')) == 3:
                return map(int, args[0].split(':'))

        elif len_args == 1 and isinstance(args[0], MyTime):
            return args[0].hours, args[0].minutes, args[0].seconds

        else:
            return 0, 0, 0

    def __eq__(self, other):
        if not self.hours == other.hours:
            return False
        if not self.minutes == other.minutes:
            return False
        if not self.seconds == other.seconds:
            return False
        return True

    def __ne__(self, other):
        if not self.hours != other.hours:
            return True
        if not self.minutes != other.minutes:
            return True
        if not self.seconds != other.seconds:
            return True
        return False

    def __ge__(self, other):
        if self.hours >= other.hours:
            return True
        if self.minutes >= other.minutes:
            return True
        if self.seconds >= other.seconds:
            return True
        return False

    def __le__(self, other):
        if self.hours <= other.hours:
            return True
        if self.minutes <= other.minutes:
            return True
        if self.seconds <= other.seconds:
            return True
        return False

    def __lt__(self, other):
        if self.hours > other.hours:
            return True
        if self.minutes > other.minutes:
            return True
        if self.seconds > other.seconds:
            return True
        return False

    def __gt__(self, other):
        if self.hours < other.hours:
            return True
        if self.minutes < other.minutes:
            return True
        if self.seconds < other.seconds:
            return True
        return False

    def __add__(self, other):
        return f'{self.hours+ other.hours}:{self.minutes + other.minutes}:{self.seconds + other.seconds} '

    def __sub__(self, other):
        return f'{self.hours - other.hours}:{self.minutes - other.minutes}:{self.seconds - other.seconds}'

    def __str__(self):
        return f'{self.hours}: {self.minutes}: {self.seconds}'


if __name__ == '__main__':
    my_time = MyTime('12:12:20')
    my_time2 = MyTime('13:11:100')
    print(my_time == my_time2)
    print(my_time != my_time2)
    print(my_time >= my_time2)
    print(my_time <= my_time2)
    print(my_time < my_time2)
    print(my_time > my_time2)
    print(my_time + my_time2)
    print(my_time - my_time2)
    print(my_time, my_time2)
