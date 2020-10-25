class MyTime:
    def __init__(self, *args):
        if len(args) == 3:
            self.hours, self.minutes, self.seconds = args
        else:
            self.hours, self.minutes, self.seconds = 0, 0, 0

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
        return f'{self.hours + other.hours}:{self.minutes + other.minutes}:{self.seconds + other.seconds}'

    def __sub__(self, other):
        return f'{self.hours - other.hours}:{self.minutes - other.minutes}:{self.seconds - other.seconds}'

    def __str__(self):
        return f'{self.hours}: {self.minutes}: {self.seconds}'


class Str(MyTime):
    def __init__(self, string_line, *args):
        super(Str, self).__init__(*args)
        self.string_line = string_line

    def __eq__(self, other):
        if self.string_line == other.string_line:
            return True
        return False

    def __ne__(self, other):
        if self.string_line != other.string_line:
            return True
        return False

    def __ge__(self, other):
        if self.string_line >= other.string_line:
            return True
        return False

    def __le__(self, other):
        if self.string_line <= other.string_line:
            return True
        return False

    def __lt__(self, other):
        if self.string_line > other.string_line:
            return True
        return False

    def __gt__(self, other):
        if self.string_line < other.string_line:
            return True
        return False

    def __add__(self, other):
        return self.string_line + other.string_line

    def __sub__(self, other):
        try:
            self.string_line - other.string_line
        except TypeError:
            print(f'нельзя выполнить : {self.string_line}-{other.string_line}')
        return False

    def __str__(self):
        return f'{self.string_line}'


class Tuples(MyTime):
    def __init__(self, my_list, *args):
        super(Tuples, self).__init__(*args)
        self.my_list = my_list

    def __cmp__(self, other):
        if self.my_list == other.my_list:
            return True
        return False

    def __ne__(self, other):
        if self.my_list != other.my_list:
            return True
        return False

    def __ge__(self, other):
        if self.my_list >= other.my_list:
            return True
        return False

    def __le__(self, other):
        if self.my_list <= other.my_list:
            return True
        return False

    def __lt__(self, other):
        if self.my_list > other.my_list:
            return True
        return False

    def __gt__(self, other):
        if self.my_list < other.my_list:
            return True
        return False

    def __add__(self, other):
        return self.my_list + other.my_list

    def __sub__(self, other):
        try:
            self.my_list - other.my_list
        except TypeError:
            print(f'нельзя выполнить : {self.my_list}-{other.my_list}')
        return False

    def __str__(self):
        return f'{self.my_list}'


class No_parameters(MyTime):
    def __init__(self, parameters=None, *args):
        super(No_parameters, self).__init__(*args)
        self.parameters = parameters

    def __cmp__(self, other):
        if self.parameters == other.parameters:
            return True
        return False

    def __ne__(self, other):
        if self.parameters != other.parameters:
            return True
        return False

    def __ge__(self, other):
        try:
            self.parameters >= other.parameters
        except TypeError:
            print(f'нельзя выполнить : {self.parameters}>={other.parameters}')
        return False

    def __le__(self, other):
        try:
            self.parameters <= other.parameters
        except TypeError:
            print(f'нельзя выполнить : {self.parameters}<={other.parameters}')
        return False

    def __lt__(self, other):
        try:
            self.parameters > other.parameters
        except TypeError:
            print(f'нельзя выполнить : {self.parameters}>{other.parameters}')
        return False

    def __gt__(self, other):
        try:
            self.parameters < other.parameters
        except TypeError:
            print(f'нельзя выполнить : {self.parameters}<{other.parameters}')
        return False

    def __add__(self, other):
        try:
            self.parameters + other.parameters
        except TypeError:
            print(f'нельзя выполнить : {self.parameters}+{other.parameters}')
        return False

    def __sub__(self, other):
        try:
            self.parameters - other.parameters
        except TypeError:
            print(f'нельзя выполнить : {self.parameters}-{other.parameters}')
        return False

    def __str__(self):
        return f'{self.parameters}'


if __name__ == '__main__':
    my_time = MyTime(12, 31, 1)
    my_time2 = MyTime(15, 31, 1)
    print(my_time == my_time2)
    print(my_time != my_time2)
    print(my_time >= my_time2)
    print(my_time <= my_time2)
    print(my_time < my_time2)
    print(my_time > my_time2)
    print(my_time + my_time2)
    print(my_time - my_time2)
    print(my_time, my_time2)

    cls_str = Str('Hello ')
    cls_str2 = Str('World')
    print(cls_str == cls_str2)
    print(cls_str != cls_str2)
    print(cls_str >= cls_str2)
    print(cls_str <= cls_str2)
    print(cls_str < cls_str2)
    print(cls_str > cls_str2)
    print(cls_str + cls_str2)
    print(cls_str - cls_str2)
    print(cls_str, cls_str2)

    tuples = Tuples([1, 2, 3])
    tuples2 = Tuples([4, 5, 6])
    print(tuples == tuples2)
    print(tuples != tuples2)
    print(tuples >= tuples2)
    print(tuples <= tuples2)
    print(tuples < tuples2)
    print(tuples > tuples2)
    print(tuples + tuples2)
    print(tuples - tuples2)
    print(tuples, tuples2)

    no_parameters = No_parameters()
    no_parameters2 = No_parameters()
    print(no_parameters == no_parameters2)
    print(no_parameters != no_parameters2)
    print(no_parameters >= no_parameters2)
    print(no_parameters <= no_parameters2)
    print(no_parameters < no_parameters2)
    print(no_parameters > no_parameters2)
    print(no_parameters + no_parameters2)
    print(no_parameters - no_parameters2)
    print(no_parameters, no_parameters2)
