import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [[x for x in s.split('=')] for s in lst_in]

d = {}

for item in lst_in:
    d[int(item[0])] = item[1]

print(*sorted(d.items()))
