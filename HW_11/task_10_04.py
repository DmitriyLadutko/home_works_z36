def replased_elements():
    with open('for file 1.txt', 'r') as my_file1:
        with open('for file 2.txt', 'w') as my_file2:

            old_element = my_file1.read()
            new_element = old_element.replace('0', '1')
            my_file2.write(new_element)

            return old_element, new_element


replased_elements()
