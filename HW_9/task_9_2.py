# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         dict_ = {key * 2: value}
#         print(f'{kwargs} -> {dict_}')
#
#
# print_values(dima=1, aaaa=1, aaa=2)

#
def print_values(**kwargs):
    for key, value in kwargs.items():
        dict_ = {key * 2: value}
        print(dict_)


print_values(dima=1, aaaa=1, aaa=2)


