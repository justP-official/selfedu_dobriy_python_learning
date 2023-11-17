nums = [float(x) for x in input().split()]
cities = input().split()
lst = [*nums, *cities]
print(*lst)
