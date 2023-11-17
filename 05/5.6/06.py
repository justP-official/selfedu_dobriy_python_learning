# сортировка выбором

a = list(map(int, input().split()))

for i in range(len(a)-1):
    m = a[i]
    p = i
    for j in range(i+1, len(a)):
        if m > a[j]:
            m = a[j]
            p = j

    if p != i:
        a[i], a[p] = a[p], a[i]

print(*a)
