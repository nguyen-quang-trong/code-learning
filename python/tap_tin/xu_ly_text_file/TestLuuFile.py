from XuLyFile import * 
import os

duongdan = os.path.join(os.path.dirname(__file__), "database.txt")

masp=input("nhập mã SP:") 
tensp=input("nhập tên sp:") 
dongia=float(input("nhập giá:")) 
line=masp+";"+tensp+";"+str(dongia) 
 
LuuFile(duongdan,line)
