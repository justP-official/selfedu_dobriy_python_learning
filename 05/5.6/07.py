# сортировка пузырьком

a = list(map(int, input().split()))

for i in range(len(a)):
    for j in range(i, len(a)):
        if a[j] < a[i]:
            a[j], a[i] = a[i], a[j]

print(*a)
