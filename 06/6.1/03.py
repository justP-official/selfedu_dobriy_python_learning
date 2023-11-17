lst = [[x for x in s.split('=')] for s in input().split()]

d = dict(lst)

if 'house' in d and 'True'  in d and  '5' in d:
    print('ДА')
else:
    print('НЕТ')
    