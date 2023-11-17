d = {}

while True:
    x = int(input())
    if x == 0:
        break
    if x in d:
        print(f"значение из кэша: {d[x]}")
    else:
        d[x] = round(x ** .5, 2)
        print(d[x])
