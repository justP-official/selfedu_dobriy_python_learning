a = list(map(float, input().split()))

lst = [x for i, x in enumerate(a) if i % 2 == 0 or i == 0]

print(lst)
