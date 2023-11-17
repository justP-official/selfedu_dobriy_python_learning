import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_in = [[x for x in s.split(':')] for s in lst_in]

s = set()

for elem in lst_in:
    s.add(elem[0])

print(len(s))
