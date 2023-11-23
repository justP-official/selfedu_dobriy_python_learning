"""
Подвиг 2. На вход поступает список целых чисел, записанных в одну строчку через пробел.
Преобразуйте сначала эту строку в список из целых чисел, а затем список в кортеж из целых чисел.
То есть, в программе будет две разные коллекции: список и кортеж.
Отсортируйте по возрастанию значений эти коллекции методом sort, если это возможно,
а иначе - примените функцию sorted.

На экран ничего выводить не нужно, только сформировать две отсортированные коллекции:
lst (список) - результат сортировки списка;
tp_lst (кортеж) - результат сортировки кортежа.

P. S. На результаты сортировок обязательно должны ссылаться переменные с именами lst и tp_lst!
"""

s = input()

lst = [int(x) for x in s.split()]

lst.sort()
tp_lst = tuple(sorted(lst))
