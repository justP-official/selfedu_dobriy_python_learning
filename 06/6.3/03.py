c = tuple(input().split())

if 'Ульяновск' in c:
    t = ()
    for x in c:
        if x != 'Ульяновск':
            t += (x,)
    print(*t)
else:
    print(*c)
