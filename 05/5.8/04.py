c = input().split()

c = [x for x in c if len(x) > 5]

print(*c)