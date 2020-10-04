original_str = input()
upper_case = 0
lover_case = 0


def dictionary_with_information_about_letters():
    global original_str
    global upper_case
    global lover_case
    for letter in original_str:
        if 'a' <= letter <= 'z':
            lover_case += 1
        elif 'A' <= letter <= 'Z':
            upper_case += 1
        elif 'а' <= letter <= 'я':
            lover_case += 1
        elif 'А' <= letter <= 'Я':
            upper_case += 1
            return dictionary_with_information_about_letters()


dictionary_with_information_about_letters()

dictionary = {lover_case: ' - Количество букв в нижнем регистре',
              upper_case: ' - Количество букв в верхнем регистре'}
print(dictionary)
