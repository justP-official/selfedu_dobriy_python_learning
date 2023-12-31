def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


lst = [int(x) for x in input().split()]

print(*filter_lst(lst))
print(*filter_lst(lst, lambda x: x < 0))
print(*filter_lst(lst, lambda x: x >= 0))
print(*filter_lst(lst, lambda x: 3 <= x <= 5 ))
