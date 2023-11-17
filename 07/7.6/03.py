a, b = map(int, input().split())

lst = [x for x in range(*(a, b+1))]
print(*lst)
