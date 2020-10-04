list_of_students = [{'firstname': 'Masha', 'Group': 42,
                     'physics': 7, 'informatics': 6, 'history': 8},
                    {'firstname': 'Dima', 'Group': 42,
                     'physics': 8, 'informatics': 7, 'history': 6},
                    {'firstname': 'Pasha', 'Group': 42,
                     'physics': 5, 'informatics': 6, 'history': 7},
                    {'firstname': 'Katia', 'Group': 42,
                     'physics': 9, 'informatics': 9, 'history': 10},
                    {'firstname': 'Nastia', 'Group': 42,
                     'physics': 10, 'informatics': 10, 'history': 10},
                    {'firstname': 'Ivan', 'Group': 42,
                     'physics': 3, 'informatics': 1, 'history': 4},
                    {'firstname': 'Vasia', 'Group': 42,
                     'physics': 3, 'informatics': 2, 'history': 3}]
result_dict = {}
for dictionary in list_of_students:
    for key in dictionary:
        try:
            result_dict[key] += dictionary[key]
        except KeyError:
            result_dict[key] = dictionary[key]

del result_dict['firstname']
del result_dict['Group']
arithmetic_mean = sum(result_dict.values())
print('Среднее арифметическое значение по всем предметам равно :', int(arithmetic_mean / 3))