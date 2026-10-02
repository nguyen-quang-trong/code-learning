# Cho mã lệnh:
# for n in oscillate(-3,5):
#     print(n,end=' ')
# print()
# Hãy viết hàm oscillate để khi chạy phần mềm, nó ra kết quả: -3 3 -2 2 -1 1 0 0 1 -1 2 -2 3 -3 4 -4

def oscillate(batdau,ketthuc):
    kq=""
    for i in range(batdau,ketthuc):
        j=i*(-1)
        kq=kq+str(i)+","+str(j)
    return kq

for n in oscillate(-3,5):
    print(n,end=' ')
print()