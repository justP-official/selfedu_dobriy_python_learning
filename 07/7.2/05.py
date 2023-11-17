def is_odd(x):
    return False if x % 2 == 0 else True


a = [int(x) for x in input().split()]

lst = [x for x in a if is_odd(x)]

print(*lst)
