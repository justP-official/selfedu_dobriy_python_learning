def is_small(s):
    return False if len(s) < 6 else True


c = input().split()

lst = [x for x in c if is_small(x)]

print(*lst)
