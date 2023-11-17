import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [[x for x in s.split()] for s in lst_in]
d = {}

for elem in lst_in:
    d.setdefault(elem[0], [])
    d[elem[0]].append(elem[1])

for k, v in d.items():
    print(f"{k}: {','.join(v)}")
