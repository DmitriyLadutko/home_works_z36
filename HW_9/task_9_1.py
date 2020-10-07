'''
Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’, где i
это порядковый номер строки в списке. Использовать генератор списков.
'''

list_of_string = ['Hello Wоrld', 'Здесь еще строка', 'И опять строка']
fin_list = []
length_my_list = len(list_of_string)

print([f'{element} -  {index}' for (element, index) in enumerate(list_of_string)])

for index in range(length_my_list):
    fin_list.append(f'{index} - {list_of_string[index]}')

print(fin_list)
