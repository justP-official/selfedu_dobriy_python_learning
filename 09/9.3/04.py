"""
Подвиг 4. На вход программы поступает строка в формате:

ключ_1=значение_1 ключ_2=значение_2 ... ключ_N=значение_N

Необходимо с помощью функции map преобразовать ее в кортеж tp вида:

tp = (('ключ_1', 'значение_1'), ('ключ_2', 'значение_2'), ..., ('ключ_N', 'значение_N'))
"""

tp = tuple(map(lambda x: tuple(x.split("=")), input().split()))

print(tp)
