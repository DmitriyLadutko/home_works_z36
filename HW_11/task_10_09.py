from csv_utils import sum_all_product,\
    determination_of_the_highest_price,\
    determination_of_the_minimal_price, \
    decrease_in_the_quantity_of_goods, \
    decrease_in_the_quantity_of_goods_input


filename = 'comment_quantity_price_product.csv'
print(f'{sum_all_product(filename=filename)} - количество всех товаров ')
print(f'{determination_of_the_highest_price(filename=filename)} - максимальная цена товаров')
print(f'{determination_of_the_minimal_price(filename=filename)} - минимальная цена товаров')
print(f'{decrease_in_the_quantity_of_goods(filename=filename)} - количество товара уменьшилось на 1')
print(f'{decrease_in_the_quantity_of_goods_input(filename=filename)} - осталось товара')
