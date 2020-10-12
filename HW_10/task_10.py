def decorating_the_function(func):
    def wrapper_function(arg1):
        print(f'Спасибо, ваши данные приняты: {list(arg1)}')
        func(arg1)
        list_range = [x for x in arg1 if x % 2 != 0]
        print(f'Ваш желаемы результат: {list_range}')

    return wrapper_function


@decorating_the_function
def function_for_decoration(arg2):
    print('Произвожу сложные математические вычисления....')


''' создал функцию, которая принимает на вход список чисел, далее она 
передается по аргументу в декоратор
там она успешно обрабатывается условием декоратора и выдает желаемый результат'''

function_for_decoration(arg1=range(20))
