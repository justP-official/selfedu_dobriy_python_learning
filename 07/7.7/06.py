def get_path(n):
    if n in (1, 2):
        return n
    return get_path(n-2) + get_path(n-1)


num = int(input())

print(get_path(num))
