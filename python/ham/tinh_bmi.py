def TinhBMI(chieucao,cannang):
    return round(cannang/(chieucao*chieucao),1)
def PhanLoai(bmi):
    if bmi<18.5: return "Gầy"
    elif bmi>=18.5 and bmi<=24.9: return "Bình thường"
    elif bmi>=25 and bmi<=29.9: return "Hơi béo"
    elif bmi>=30 and bmi<=34.9: return "Béo phì cấp độ 1"
    elif bmi>=35.0 and bmi<=39.9: return "Béo phì cấp độ 2"
    return "Béo phì cấp độ 3"
def CanhBaoBenh(bmi):
    if bmi<18.5: return "Thấp"
    elif bmi>=18.5 and bmi<=24.9: return "Trung bình"
    elif bmi>=25 and bmi<=29.9: return "Cao"
    elif bmi>=30 and bmi<=34.9: return "Cao"
    elif bmi>=35.0 and bmi<=39.9: return "Rất cao"
    return "Nguy hiểm"

chieucao=float(input("Chieu cao: "))
cannang=float(input("Can nang: "))
bmi=TinhBMI(chieucao,cannang)
print("Phân loại: ",PhanLoai(bmi))
print("Nguy cơ phát triển bệnh: ",CanhBaoBenh(bmi))