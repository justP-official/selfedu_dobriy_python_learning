n = int(input())

lst = [[i for _ in range(n)] for i in range(n)]

for row in lst:
    print(*row)
