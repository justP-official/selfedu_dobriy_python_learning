def mul_max_and_min(maximum, minimum):
    return maximum * minimum


a = [int(x) for x in input().split()]

print(mul_max_and_min(max(a), min(a)))
