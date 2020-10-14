def file_6_lines(file: str):
    with open(file, 'w') as my_file:
        my_file.writelines([input('input 1 line \n'), input('input 2 line \n'),
                            input('input 3 line \n'), input('input 4 line \n'),
                            input('input 5 line \n'), input('input 6 line \n')])
    return file_6_lines


file_6_lines('new.txt')
