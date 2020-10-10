from datetime import datetime


def decorating(fun):
    def wrapper_function():
        time = datetime.now()
        fun()
        print(f'Время на выполение {datetime.now() - time}')
        return fun

    return wrapper_function


''' импортировал модуль datetime 
в декорируемой функции вывел текущее время
в декораторе посчитал время на выполнение и вывел'''


@decorating
def decor_fun():
    print(f'Текущее время {datetime.now()}')


decor_fun()
