def ToiUuChuoi(s):
    tmp=""
    for i in range(len(s)):
        if s[i]==" " and (tmp=="" or s[i-1]==" "):continue
        else: tmp=tmp+s[i]
    s=tmp
    if tmp[len(tmp)-1]==" ":
        s=""
        for i in range(len(tmp)-1): s=s+tmp[i]
    return s

s=input("Nhap chuoi: ")
print("Chuoi toi uu:",len(s)," =>",  len(ToiUuChuoi(s)))