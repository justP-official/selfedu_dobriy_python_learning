"""
Подвиг 5. Вводится таблица целых чисел, записанных через пробел.
Необходимо перемешать столбцы этой таблицы, используя функции shuffle и zip и вывести результат на экран (также в виде таблицы).
"""

import sys
import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst = [list(map(int, x.split())) for x in lst_in]

matrix = list(map(list, zip(*lst)))

random.shuffle(matrix)

matrix = zip(*matrix)

for row in matrix:
    print(*row)

