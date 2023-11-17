numbers_lst = input().split()

d = {}
for i in range(len(numbers_lst)):
    kod = numbers_lst[i][:2]
    if kod in d:
        d[kod].append(numbers_lst[i])
    else:
        d[kod] = [numbers_lst[i]]

print(*sorted(d.items()))
