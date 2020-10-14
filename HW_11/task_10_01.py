from itertools import islice


def print_first_line(file_name: str):
    my_file = open(file_name)
    line = my_file.readline()

    if line:
        print(line)

    my_file.close()


print_first_line('aaa.txt')


def print_selected_line(file_name: str, line_number: int):
    my_file = open(file_name)
    counter = 0
    while counter != line_number:
        line = my_file.readline()
        if not line:
            print('File size is less than', line_number)
            break
        if counter + 1 == line_number:
            print(line.strip())

        counter += 1
    my_file.close()


print_selected_line('aaa.txt', 5)


def print_lines_1_5(file: str):
    with open(file) as my_file:
        lines = [next(my_file) for x in range(5)]
        print(f'{str(lines)} первые 5 строк')


print_lines_1_5('aaa.txt')


def print_lines_1_5_ver_2(file: str):
    with open(file) as myfile:
        lines = list(islice(myfile, 5))
    print(lines, '2 version')


print_lines_1_5_ver_2('aaa.txt')


def print_lines_1_2(file: str):
    with open(file) as my_file:
        lines = [next(my_file) for x in range(0, 2)]
        print(f'{lines} строки с s1-й по s2-ю')


print_lines_1_2('aaa.txt')


def print_all_file(file: str):
    with open(file) as my_file:
        for line in my_file.readlines():
            print(line.strip())

    print('ALl FILE')


print_all_file('aaa.txt')
