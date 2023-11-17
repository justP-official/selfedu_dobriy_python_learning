def get_line_list(d, a=[]):
    for elem in d:
        if type(elem) != list:
            a.append(elem)
        else:
            get_line_list(elem, a)

    return a


d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
print(get_line_list(d))
