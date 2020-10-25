def finding_differences(file1: str, file2: str):
    with open(file1, 'r') as my_file:
        line1 = set(enumerate(my_file.readlines()))
        with open(file2, 'r') as my_file2:
            line2 = set(enumerate(my_file2.readlines()))
            for num, x in line1 - line2:
                print(f'{num} - номер строки в которой есть отличия')


finding_differences(file1='file 1.txt', file2='file 2.txt')
