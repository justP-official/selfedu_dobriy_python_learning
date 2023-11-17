import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

lst = [x for row in lst_in[::-1] for x in row[::-1]]

print(*lst)
