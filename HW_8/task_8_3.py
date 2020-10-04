# def function_defining_palindrome(word_1, word_2, word_3):
#     if word_1 == word_1[:: -1]:
#         print(f'{word_1} Является полиндромом')
#     else:
#         print(f'{word_1} Не является полиндромом')
#     if word_2 == word_2[:: -1]:
#         print(f'{word_2} Является полиндромом')
#     else:
#         print(f'{word_2} Не является полиндромом')
#     if word_3 == word_3[:: -1]:
#         print(f'{word_3} Является полиндромом')
#     else:
#         print(f'{word_3} Не является полиндромом')
#
#
# function_defining_palindrome(word_1=input(), word_2=input(), word_3=input())


def palindrom(word):
    if word == word[:: -1]:
        print(f'{word} Является полиндромом')
    else:
        print(f'{word} Неявляется полиндромом')
    return word == word[::-1]


palindrom(word=input())
