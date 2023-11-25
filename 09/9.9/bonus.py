"""
Написать программу, которая определяет есть ли выйгрышные позиции у крестиков в игре "Крестики - Нолики"
"""


def true_x(a):
    return a == 'x'


p = ['x', 'x', 'o',
     'o', 'x', 'o',
     'x', 'x', 'x']

row_1 = all(map(true_x, p[:3]))
row_2 = all(map(true_x, p[3:6]))
row_3 = all(map(true_x, p[6:]))

col_1 = all(map(true_x, p[::3]))
col_2 = all(map(true_x, p[1::3]))
col_3 = all(map(true_x, p[2::3]))

left_diagonal = all(map(true_x, p[::4]))
right_diagonal = all(map(true_x, p[2:7:2]))
