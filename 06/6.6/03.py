lst = input().lower().split()

s = {c for c in lst if len(c) > 3}

print(len(s))
