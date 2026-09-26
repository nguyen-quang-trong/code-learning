def TinhROI(doanhthu,chiphi):
    return (doanhthu-chiphi)/chiphi
def GoiYDauTu(roi):
    if roi>=0.75: print("Bạn nên đầu tư dự án")
    else: print("Bạn không nên đầu tư dự án")

doanhthu=float(input("Doanh thu: "))
chiphi=float(input("Chi phi: "))
roi=TinhROI(doanhthu,chiphi)
print("Tỉ lệ ROI: ",roi," => ",end='')
GoiYDauTu(roi)