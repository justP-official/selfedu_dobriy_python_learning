n = int(input())

lst = [[1 if i == j else 0 for i in range(n)] for j in range(n)]

for row in lst:
    print(*row)
