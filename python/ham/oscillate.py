def oscillate(batdau,ketthuc):
    kq=""
    for i in range(batdau,ketthuc):
        j=i*(-1)
        kq=kq+str(i)+","+str(j)
    return kq

for n in oscillate(-3,5):
    print(n,end=' ')
print()