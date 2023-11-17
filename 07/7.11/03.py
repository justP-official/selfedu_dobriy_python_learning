def sort_list(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sorted(res)
    return wrapper


@sort_list
def get_list(s):
    return [int(x) for x in s.split()]


lst = get_list(input())

print(*lst)
