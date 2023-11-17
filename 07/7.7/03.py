def fib_rec(N, f=[]):
    if len(f) < 2:
        f.append(1)
    elif len(f) < N:
        f.append(f[-1] + f[-2])
    if len(f) < N:
        return fib_rec(N, f)
    return f


n = int(input())

print(fib_rec(n))
