lst = input().split()

lst = [[x for x in s.split('=')] for s in lst]

d = dict(lst)

for i in d:
    d[i] = int(d[i])

print(*sorted(d.items()))


