c = input().split()

lst = [[c[i]] + [int(c[i+1])] for i in range(0, len(c), 2)]

print(lst)
