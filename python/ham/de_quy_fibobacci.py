def TimSoFib(n):
    if n in (0,1): return 1
    else:
        return TimSoFib(n-1)+TimSoFib(n-2)
def XuatSoFib(n):
    print("Day so Fib: ",end='')
    for i in range(n+1):
        if i==0: print("1 ",end='')
        else: print("->",TimSoFib(i),end=' ')

vt=int(input("Nhập vị trí: "))
print("So Fib la: ",TimSoFib(vt))
XuatSoFib(vt)
print()