set /p SoMayCuaDoanhNghiep=Nhap so may cua doanh nghiep: 
set /a SoMayCuaDoanhNghiep=%SoMayCuaDoanhNghiep%+2
set HostID=2
set TrangThai=4

:TimHostID
if %TrangThai% GEQ %SoMayCuaDoanhNghiep% Goto StopTimHostID
set /a HostID=%HostID%+1
set /a TrangThai=%TrangThai%*2
Goto TimHostID
:StopTimHostID
set LopMang=A
if %HostID% LEQ 16 set LopMang=B
if %HostID% LEQ 8 set LopMang=C

echo HostID nho nhat la %HostID%
echo So dia chi co the cap la %TrangThai%
echo Lop mang toi uu la %LopMang%