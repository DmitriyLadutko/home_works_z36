text = 'The Zen of Python, by Tim Peters\n' \
       'Beautiful is better than ugly.\n' \
       'Explicit is better than implicit.\n' \
       'Simple is better than complex.\n Complex is better than complicated.\n' \
       'Flat is better than nested.\n' \
       'Sparse is better than dense.\n ' \
       'Readability counts.\n' \
       'Special cases aren"t special enough to break the rules.\n ' \
       'Although practicality beats purity.\n' \
       'Errors should never pass silently.\n ' \
       'Unless explicitly silenced.\n' \
       'In the face of ambiguity, refuse the temptation to guess.\n ' \
       'There should be one-- and preferably only one --obvious way to do it.\n' \
       ' Although that way may not be obvious at first unless you"re Dutch.\n' \
       'Now is better than never.\n ' \
       'Although never is often better than *right* now.\n ' \
       'If the implementation is hard to explain, it"s a bad idea.\n ' \
       'If the implementation is easy to explain, it may be a good idea. \n ' \
       'Namespaces are one honking great idea -- let"s do more of those!' \
       + 'Aziraal007@yandex.ru'

letter = 0
vowels = 'aeoiuyAEJIUY'
alfavit = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowel_counter = 0
every_18_character = text[::18]

for x in text:
    if x in alfavit:
        letter += 1
print(f'{letter}  - количество всех букв')

for i in text:
    if i in vowels:
        vowel_counter += 1
print(f'{vowel_counter}  - количество всех гласных')

for element in range(len(text)):
    if element % 18 == 0:
        print(element, text.swapcase()[element])
