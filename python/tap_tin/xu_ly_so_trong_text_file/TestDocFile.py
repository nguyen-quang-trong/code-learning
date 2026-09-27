from  XuLyFile import * 
import os

duongdan = os.path.join(os.path.dirname(__file__), "csdl_so.txt")
arrSo=DocFile(duongdan) 
print(arrSo) 
def XuatSoAmTrenMoiDong(arrSo): 
    for row in arrSo: 
        for element in row: 
            number=int(element) 
            if number<0: 
                print(number,end='\t') 
        print()
print("Các số âm trên mỗi dòng:") 
XuatSoAmTrenMoiDong(arrSo)
