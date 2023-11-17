names = tuple(input().lower().split())

t = (n for n in names if 'ва' in n)

print(*t)
