def counter_add():
    def increase(x):
        x += 5
        return x

    return increase


cnt = counter_add()
k = int(input())

print(cnt(k))
