import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = [[x for x in s.split()] for s in lst_in]

menu = ()

for elem in lst_in:
    menu += (tuple(elem), )

print(menu)
