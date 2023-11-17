n = int(input())

lst = [x for x in range(1, n) if n % x == 0] + [n]

print(*lst)