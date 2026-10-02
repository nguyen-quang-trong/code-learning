for d in range(4):
    for c in range(4):
        if d in (1,2) and c in (1,2):print('',end=' ')
        else:print('*',end='')
    print()
print()

for d in range(4):
    c=3-d
    for i in range(c): print('',end=' ')
    for i in range(d+1): print('*',end='')
    print()
print()

for d in range(7):
    for c in range(7):
        if d==c: print('*',end='')
        elif (c==0 and d in (1,2,3)) or (c==6 and d in (3,4,5)) or (d==3): print('*',end='')
        else: print('',end=' ')
    print()
