# Nhập vào số giây bất kỳ t. Tính và xuất ra dạng Giờ:Phút:Giây.
# Ví dụ: Nhập 3750 thì xuất ra 1:2:30 AM; nhập 51100 thì xuất ra 2:11:40 PM.

t=int(input("Nhập số giây:")) 
hour=(t//3600)%24 
minute=(t%3600)//60 
second=(t%3600)%60 
print(hour,":",minute,":",second)
