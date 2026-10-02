# Cho 1 Chuỗi như sau “5;7;8;-2;8;11;13;9;10” (có thể nhập bất kỳ từ bàn phím ) 
# - xuất các chữ số trên các dòng riêng biệt 
# - Xuất có bao nhiêu chữ số chẵn  
# - Xuất có bao nhiêu số âm  
# - Xuất có bao nhiêu chữ số nguyên tố 
# - Tính giá trị trung bình

def ktSoChan(so):
    if abs(so%2)==0:return True
    return False
def ktSoNguyenTo(so):
    if so<=0: return False
    for i in range(2,so//2):
        if so%i==0: return False
    return True

s="5;7;8;-2;8;11;13;9;10"
kytu=""
s2=""
demsochan=0
demsole=0
demsonguyento=0
tong=0
for i in range(len(s)):
    if s[i]!=";": kytu=kytu+s[i]
    if s[i]==";" or i+1==len(s):
        s2=s2+kytu+"\n"
        so=int(kytu)
        if ktSoChan(so):demsochan+=1
        else: demsole+=1
        if ktSoNguyenTo(so):demsonguyento+=1
        tong=tong+so
        kytu=""
tb=tong/(demsochan+demsole)
print("Xuat cac chu so tren cac dong rieng biet:",end='\n')
print(s2)
print("So chu so chan: ",demsochan)
print("So chu so le: ",demsole)
print("So chu so nguyen to: ",demsonguyento)
print("Gia tri trung binh: ",tb)