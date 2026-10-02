# Viết lại đoạn code bằng cách dùng từ khóa break thay thế biến done:
# 
# done = False
# n, m = 0, 100
# while not done and n != m:
#   n = int(input())
#   if n < 0:
#     done = True
#   print("n =", n)

n,m=0,100
while n!=m:
    n=int(input())
    if n<0: break
    print("n=",n)
