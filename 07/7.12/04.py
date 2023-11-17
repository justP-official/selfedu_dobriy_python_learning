from functools import wraps


def calculate_sum(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return sum(func(*args))

    return wrapper


@calculate_sum
def get_list(s):
    '''Функция для формирования списка целых значений'''

    return [int(x) for x in s.split()]


s = get_list("1 2 3 -1 -2 -3")
print(s)