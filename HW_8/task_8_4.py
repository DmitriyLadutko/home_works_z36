text = 'import this ' + 'Aziraal007@yandex.ru'
len_text = len(text)
print(len_text)
letter = 0
vowels = ['a', 'e', 'o', 'i', 'u', 'y']
vowel_counter = 0
every_18_character = text[18]

for x in text:
    if 'a' <= x <= 'z':
        letter += 1
    elif 'A' <= x <= 'Z':
        letter += 1
print(f'{letter}  - количество всех букв')

'''
Инкрементим счетчик пока переменная х лежит в указанном диапозоне
'''

for i in text:
    if i in vowels:
        vowel_counter += 1
print(f'{vowel_counter}  - количество всех гласных')

'''
Инкрементим счетчик пока переменная i лежит в указанном диапозоне
'''

for y in every_18_character:
    if 'a' <= y <= 'z':
        print(f'{every_18_character.upper()} {18}')
    elif 'A' <= y <= 'Z':
        print(f'{every_18_character.lower()} {18}')
