"""
Подвиг 3. Вводится таблица целых чисел.
Используя функцию map и генератор списков, преобразуйте список строк lst_in в двумерный список с именем lst2D,
содержащий целые числа.

Выводить на экран ничего не нужно, только сформировать список lst2D на основе введенных данных.
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))


def make_2d(x):
    return [int(x) for x in x.split()]


lst2D = list(map(make_2d, lst_in))
# print(lst2D)
