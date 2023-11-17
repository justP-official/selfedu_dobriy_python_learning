"""
Подвиг 4.
В программе имеется функция factorial.
В начале программы (до определения функции) необходимо из модуля math импортировать функцию с тем же именем factorial, используя команду from, но так, чтобы они не "затирали" друг друга.
Имя импортируемой функции в модуле (программе) должно быть fact.
"""

from math import factorial as fact


def factorial(n):
    p = 1
    for i in range(2, n+1):
        p *= i

    print("my factorial")
    return p

