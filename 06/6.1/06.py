import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_in = [[x for x in s.split()] for s in lst_in]
d = {}
for i in range(len(lst_in)):
    kod = lst_in[i][1]
    if kod in d:
        d[kod].append(lst_in[i][0])
    else:
        d[kod] = [lst_in[i][0]]

print(*sorted(d.items()))
