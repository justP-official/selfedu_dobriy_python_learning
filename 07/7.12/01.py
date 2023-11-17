def sum_dec(start=0):
    def calc_sum(func):
        def wrapper(*args, **kwargs):
            res = func(*args)
            return start + sum(res)

        return wrapper

    return calc_sum


@sum_dec(start=5)
def get_list(s: str):
    return [int(x) for x in s.split()]


s = input()
print(get_list(s))
