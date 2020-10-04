def function_defining_palindrome(word_1, word_2, word_3):
    if word_1 == word_1[:: -1]:
        print('Является полиндромом')
    else:
        print('Не является полиндромом')
    if word_2 == word_3[:: -1]:
        print('Является полиндромом')
    else:
        print('Не является полиндромом')
    if word_3 == word_3[:: -1]:
        print('Является полиндромом')
    else:
        print('Не является полиндромом')


function_defining_palindrome(word_1=input(), word_2=input(), word_3=input())
