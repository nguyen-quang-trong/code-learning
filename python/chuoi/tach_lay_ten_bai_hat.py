def LayTenFile(s):
    tmp=""
    for i in range(len(s)-1,-1,-1):
        if s[i]=="\\":break
        else:
            tmp=tmp+s[i]
    s=""
    for i in range(len(tmp)-1,-1,-1): s=s+tmp[i]
    return s

def LayTen(s):
    tmp=LayTenFile(s)
    s=""
    for i in range(len(tmp)):
        if tmp[i]==".": break
        else: s=s+tmp[i]
    return s

s=input("Nhap duong dan file: ")
print("Ten file bai hat:",LayTenFile(s))
print("Ten bai hat:",LayTen(s))