import time

def VeHinh(hinh):
    for d in range(7):
        for c in range(7):
            if hinh in (1,2):
                if d==3 or (c==3 and d in range(4)) or (c==0 and d in range(3,7)) or (d<3 and c==(d+3)) or (d>2 and c==(6-d)) or (hinh==1 and ((d==4 and c==1) or (d==2 and c==4))): print("* ",end='')
                else: print("  ",end='')
            else:
                if c==3 or (c==6-d) or (d==0 and c>3) or (d==6 and c<3) or (hinh==3 and ((d==1 and c==4) or (d==5 and c==2))): print("* ",end='')
                else: print("  ",end='')

        print()

hinh=1
while True:
    if hinh>=5:hinh=1
    VeHinh(hinh)
    print()
    time.sleep(5)
    hinh+=1