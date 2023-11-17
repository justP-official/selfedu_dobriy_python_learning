def counter_add(n):
    def increase(x):
        nonlocal n
        x += n
        return x

    return increase


cnt = counter_add(2)
k = int(input())

print(cnt(k))
