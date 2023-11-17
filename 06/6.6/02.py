import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {x for x in lst_in}

print(len(d))
