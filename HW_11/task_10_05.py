with open('original file.txt', 'r') as my_file1:
    with open('even lines.txt', 'w') as my_file2:
        with open('not even lines.txt', 'w') as my_file3:
            original_line = my_file1.readlines()
            my_file2.writelines(original_line[::2])
            my_file3.writelines(original_line[1::2])
