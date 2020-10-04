list_1 = ['*', '**', '***', '****', '*****']
list_2 = ['****', '***', '**', '*']
for key in list_1:
    if len(key) >= 1:
        print(key)
for key_2 in list_2:
    if len(key_2) >= 1:
        print(key_2)


print()
'''
Как по мне это был самы простой и очевидный способ
'''

list_1 = ['*', '**', '***', '****', '*****']
list_2 = list_1[:: -1]
for key in list_1:
    if len(key) >= 1:
        print(key)
for key_2 in list_2:
    if len(key_2) != 5 >= 1:
        print(key_2)


print()


list_1 = ['*', '**', '***', '****', '*****']
list_2 = list_1[:: -1]
[print(key) for key in list_1 if len(key) >= 1]
[print(key_2)for key_2 in list_2 if len(key_2) != 5 >= 1]