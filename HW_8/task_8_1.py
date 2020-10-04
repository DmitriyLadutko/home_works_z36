original_list = [1, 2, 3, 4, 1, 2, 6, 'Hello World!', 'Hello World!', 'i love питон', 'i love питон']


def unique_list(list_of_unique_values: list) -> list:
    list_of_unique_values = list(set(original_list))
    print(list_of_unique_values)
    return list_of_unique_values


unique_list(list_of_unique_values=[])


# как вариант можно и это

# original_list = [1, 2, 3, 4, 1, 2, 6, 'Hello World!', 'Hello World!', 'i love питон', 'i love питон']
# list_of_unique_values = list(set(original_list))
# print(list_of_unique_values)
