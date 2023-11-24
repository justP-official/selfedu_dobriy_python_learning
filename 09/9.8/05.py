"""
Подвиг 5. Определите функцию с именем get_list_dig,
которая возвращает список только из числовых значений переданной ей коллекции (список или кортеж).

Сигнатура функции должна быть, следующей:

def get_list_dig(lst): ...

Вызывать функцию не нужно, только определить. Также ничего не нужно выводить на экран.
"""


def get_list_dig(lst):
    return list(filter(lambda x: type(x) in (int, float), lst))