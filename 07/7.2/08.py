def calculate_length_of_string(s):
    return s, len(s)


c = input().split()

d = {k: v for k, v in [calculate_length_of_string(s) for s in c]}

a = sorted(d, key=lambda x: d[x])
print(*a)
