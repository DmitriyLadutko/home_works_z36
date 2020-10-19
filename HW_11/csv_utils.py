import csv
from typing import List
import pandas as pd

'Импортировал библиотеки csv, typing, pandas, для pandas дал сокращенное название при обращении pd'

__all__ = [
    'reading_csv_file',
    'writing_file',
    'append_in_csv_file',
    'adding_by_position_in_csv_file',
    'deleting_the_3_line',
    'deleting_the_last_line',
    'sum_all_product',
    'determination_of_the_highest_price',
    'determination_of_the_minimal_price',
    'decrease_in_the_quantity_of_goods',
    'decrease_in_the_quantity_of_goods_input'
]


# Функция для чтения csv файла без использования модуля pandas
def reading_csv_file(*, filename: str):
    rows = []
    with open(filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        fields = next(csv_reader)
        for row in csv_reader:
            rows.append(row)

    return fields, rows


# Функция для записи csv файла без использования модуля pandas
def writing_file(*, filename: str, fields: List, rows_list: List[List]):
    with open(filename, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows_list)


# Функция для добавления строки в конец csv файла без использования модуля pandas
def append_in_csv_file(*, filename: str, rows_list: List[List]):
    with open(filename, 'a') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows_list)


# Функция для позиционного добавления строки в csv файл с использованием модуля pandas
def adding_by_position_in_csv_file(*, filename: str, rows: List):
    read_df_csv = pd.read_csv(filename, header=0)
    read_df_csv.loc[3] = rows
    read_df_csv.to_csv(filename, header=True, sep=',', index=False)


# Функция для удаления 3-ей строки в csv файле с использованием модуля pandas
def deleting_the_3_line(*, filename: str):
    read_df_csv = pd.read_csv(filename, header=0)
    read_df_csv.drop([3], axis=0, inplace=True)
    read_df_csv.to_csv(filename, header=True, sep=',', index=False)


# Функция для удаления последней строки в csv файле с использованием модуля pandas
def deleting_the_last_line(*, filename: str):
    read_df_csv = pd.read_csv(filename, header=0)
    read_df_csv.drop(read_df_csv.index[len(read_df_csv) - 1], axis=0, inplace=True)
    read_df_csv.to_csv(filename, header=True, sep=',', index=False)


# ----------------------task_10_09------------------------
# Функция для нахождения суммы количества товар с использованием модуля pandas
def sum_all_product(*, filename: str):
    read_df_csv = pd.read_csv(filename, header=0)
    sum_elem = read_df_csv['Количество'].sum()

    return sum_elem


# Функция для нахождения максимального значения цены товара с использованием модуля pandas
def determination_of_the_highest_price(*, filename: str):
    read_df_csv = pd.read_csv(filename, header=0)
    most_expensive_product = read_df_csv['Цена'].max()

    return most_expensive_product


# Функция для нахождения минимального значения цены товара с использованием модуля pandas
def determination_of_the_minimal_price(*, filename: str):
    read_df_csv = pd.read_csv(filename, header=0)
    minimal_price = read_df_csv['Цена'].min()

    return minimal_price


# Функция, уменьшающая значение количества товара на 1 с использованием модуля pandas
def decrease_in_the_quantity_of_goods(*, filename: str):
    read_df_csv = pd.read_csv(filename, header=0)
    count = []
    decrease_in_quantity = read_df_csv['Количество']
    for i in decrease_in_quantity:
        i -= 1
        count.append(i)

    return count


# Функция, уменьшающая значение количества товара на n, n число вводит пользователь с использованием модуля pandas
def decrease_in_the_quantity_of_goods_input(*, filename: str):
    read_df_csv = pd.read_csv(filename, header=0)
    count = []
    decrease_in_quantity = read_df_csv['Количество']
    for i in decrease_in_quantity:
        i -= int(input('Введите число на которое стоит уменьшить количество товара :'))
        count.append(i)

    return count
