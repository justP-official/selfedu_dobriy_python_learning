"""
Подвиг 9. На вход программы подается целое десятичное число.
Используя битовые операции, проверьте, включен ли 5-й или 1-й биты введенного числа.
Если включен хотя бы один из этих битов, то выведите слово ДА, иначе - слово НЕТ.
"""


flags = int(input())

mask1 = 32
mask2 = 2

print('ДА' if flags & mask1 == mask1 or flags & mask2 == mask2 else 'НЕТ')
