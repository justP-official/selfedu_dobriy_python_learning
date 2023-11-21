"""
Подвиг 4. Вводится натуральное число N. Используя строки из латинских букв ascii_lowercase и ascii_uppercase:

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase
задайте функцию-генератор, которая бы возвращала случайно сформированные email-адреса с доменом mail.ru и длиной в N символов. Например, при N=6, получим адрес: SCrUZo@mail.ru

Для формирования случайного индекса для строки chars используйте функцию randint модуля random:

import random
random.seed(1)
indx = random.randint(0, len(chars)-1)
Функция-генератор должна возвращать бесконечное число таких адресов, то есть, генерировать постоянно. Выведите первые пять сгенерированных email и выведите их в столбик (каждый с новой строки).
"""

import random

from string import ascii_lowercase, ascii_uppercase
chars = ascii_lowercase + ascii_uppercase

random.seed(1)


def generate_email(n):
    res = ""
    for x in range(n):
        indx = random.randint(0, len(chars) - 1)
        res += chars[indx]

    yield res + '@mail.ru'


length = int(input())

for _ in range(5):
    g = generate_email(length)
    for x in g:
        print(x)