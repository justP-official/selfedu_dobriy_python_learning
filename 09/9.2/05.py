"""
Подвиг 5. Определите функцию-генератор, которая бы возвращала простые числа.
(Простое число - это натуральное число, которое делится только на себя и на 1).
Выведите с помощью этой функции первые 20 простых чисел (начиная с 2) в одну строчку через пробел.
"""


def get_simple():
    for number in range(2, 1000):
        for divider in range(2, number):
            if number % divider == 0:
                break
        else:
            yield number


g = get_simple()
for _ in range(20):
    print(next(g), end=' ')

