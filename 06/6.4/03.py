s = set(input())

a = []

for c in s:
    if c.isdigit():
        a.append(c)

if a:
    print(*sorted(a))
else:
    print("НЕТ")
