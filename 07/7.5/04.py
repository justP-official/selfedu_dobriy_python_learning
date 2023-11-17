def verify(args):
    for i in range(len(args) - 1):
        for j in range(len(args)):
            if args[i][j] == 1:
                if not is_isolate(args, i, j):
                    return False
    return True


def is_isolate(arr, x, y):
    n = len(arr)
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < n and 0 <= y + j < n:
                if (i or j) and arr[x + i][y + j]:
                    return False
    return True
# def is_isolate(row1, row2):
#     for i in range(len(row1)):
#         if row1[i] + row2[i] > 1 or row1[i] + row2[i-1] > 1:
#             return False
#     else:
#         return True


print(verify([1]))
