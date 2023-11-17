a = list(map(int, input().split()))
n = int(len(a) ** .5)
lst = [[a[n*i+j] for j in range(n)] for i in range(n)]

print(lst)
