n = int(input())

coins = [64, 32, 16, 8, 4, 2, 1]

summa = []

for coin in coins:
    while n >= coin:
        n -= coin
        summa.append(coin)

print(*summa)
