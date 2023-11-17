lst = [[x for x in s.split('=')] for s in input().split()]

d = dict(lst)

if 'False' in d:
    del d['False']

if '3' in d:
    del d['3']
# for item in d:
#     if item ==  or item == '3':
#         del d[item]

print(*sorted(d.items()))