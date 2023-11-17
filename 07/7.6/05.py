import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
d = {k: v for k, v in [x.split("=") for x in lst_in]}

menu = {**menu, **d}
