c = tuple(input().split())

if 'Москва' not in c:
    c += ('Москва',)

print(*c)
