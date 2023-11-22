"""
Подвиг 2. Вводится неравномерная таблица целых чисел.
С помощью функции zip выровнить эту таблицу, приведя ее к прямоугольному виду, отбросив выходящие элементы.
Вывести результат на экран в виде такой же таблицы чисел.
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = tuple(map(lambda s: s.split(), lst_in))

matrix = zip(*zip(*lst_in))

for row in matrix:
    print(*row)
