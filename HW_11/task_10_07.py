import json

'''Импортировал модуль  json'''
import random

'''Импортировал модуль  random'''

number_rows = 3
number_columns = 3
random_matrix = [random.randint(1, 10) for j in range(number_rows) for i in range(number_columns)]
'''Создал список случайных чисел'''


# ----------------------С использованием конструкции With() as-------------------------

def finding_and_overwriting_even_elements(file1, file2, file3):
    with open(file1, mode='w', encoding='UTF-8') as my_file:
        json.dump(random_matrix, my_file)
        '''Открыл файл на запись и обновил в нем информацию'''

    with open(file2, mode='r', encoding='UTF-8') as my_file2:
        data = json.load(my_file2)
        '''Открыл файл на чтение '''

    with open(file3, mode='w', encoding='UTF-8') as my_file3:
        '''Открыл файл на запись и выполнил условие '''
        for i in data:
            if i % 2 != 0:
                json.dump(i, my_file3)
    print('Все нечетные числа перезаписаны')


finding_and_overwriting_even_elements(file1='task_10_07.txt', file2='task_10_07.txt', file3='task_10_07_.txt')

# ----------------------без использования конструкции With() as-------------------------


# file_name = 'task_10_07.txt'
# my_file = open(file_name, 'w')
# file_name_2 = 'task_10_07_.txt'
# my_file_2 = open('task_10_07_.txt', 'w')
#
# json.dump(random_matrix, my_file)
# my_file.close()
#
# my_file = open(file_name, 'r')
# data = json.load(my_file)
#
# for i in data:
#     if i % 2 != 0:
#         json.dump(i, my_file_2)
# print('Все нечетные числа перезаписаны')
