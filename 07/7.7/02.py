def get_rec_sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + get_rec_sum(lst[1:])


a = [int(x) for x in input().split()]

print(get_rec_sum(a))
