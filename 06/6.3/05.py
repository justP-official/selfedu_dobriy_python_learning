n = tuple(map(int, input().split()))

t = ()

for x in n:
    if x not in t:
      t += (x,)

print(*t)
