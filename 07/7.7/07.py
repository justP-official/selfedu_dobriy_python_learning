def divide_array(lst):
    mid = len(lst) // 2
    arr_left = lst[:mid]
    arr_right = lst[mid:]
    if len(arr_left) > 1:
        arr_left = divide_array(arr_left)
    if len(arr_right) > 1:
        arr_right = divide_array(arr_right)

    return sort_union(arr_left, arr_right)


def sort_union(lst1, lst2):
    res = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            res.append(lst1[i])
            i += 1
        else:
            res.append(lst2[j])
            j += 1
    res += lst1[i:] + lst2[j:]
    return res


a = [int(x) for x in input().split()]
print(*divide_array(a))
