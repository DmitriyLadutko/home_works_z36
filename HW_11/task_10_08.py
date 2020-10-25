from csv_utils import reading_csv_file, \
    writing_file, \
    append_in_csv_file,\
    adding_by_position_in_csv_file, \
    deleting_the_3_line,\
    deleting_the_last_line
# Импорт библиотек из csv_utils

filename = 'comment_quantity_price_product.csv'
fields = ['Продукт', 'Цена', 'Количество', 'Комментарий']
rows_apple = ['Apple', 5, '2', 'No phone']
rows_pear = [
    ['Pear', 5, '5', 'fresh'],
    ['Bananas', 4, '5', 'fresh']
]
rows_melon = [
    ['melon', 3, '1', 'fresh'],
    ['Bananas', 4, '5', 'fresh'],
    ['watermelon', 3, '1', 'fresh'],
]

writing_file(filename=filename, fields=fields, rows_list=rows_pear)

append_in_csv_file(filename=filename, rows_list=rows_melon)

adding_by_position_in_csv_file(filename=filename, rows=rows_apple)

deleting_the_3_line(filename=filename)

# deleting_the_last_line(filename=filename)
