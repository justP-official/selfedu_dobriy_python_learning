def make_dict(func):
    def wrapper(*args, **kwargs):
        lst1, lst2 = func(*args)
        d = {}
        for i in range(len(lst1)):
            d[lst1[i]] = lst2[i]
        return d
    return wrapper


@make_dict
def get_lists(s1, s2):
    lst1, lst2 = s1.split(), s2.split()
    return lst1, lst2


str1 = input()
str2 = input()

d = get_lists(str1, str2)
print(*sorted(d.items()))
