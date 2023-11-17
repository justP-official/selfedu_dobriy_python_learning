def fact_rec(n):
    if n <= 0:
        return 1
    return n * fact_rec(n-1)


