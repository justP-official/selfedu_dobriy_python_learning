"""
Подвиг 3. Вводится таблица целых чисел.
Необходимо сначала эту таблицу представить двумерным списком чисел,
а затем, с помощью функции zip выполнить транспонирование этой таблицы
(то есть, строки заменить на соответствующие столбцы).
Результат вывести на экран в виде таблицы чисел (числа в строках следуют через пробел).
"""

import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = map(lambda s: s.split(), lst_in)

matrix = zip(*lst_in)

for row in matrix:
    print(*row)
