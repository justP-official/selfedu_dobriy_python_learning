def get_data_fig(*args, **kwargs):
    per = sum(args)
    params = [kwargs[k] for k in ('type', 'color', 'closed', 'width') if k in kwargs.keys()]
    res = (per, )
    for x in params:
        res += x,
    return res

print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))
print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))
