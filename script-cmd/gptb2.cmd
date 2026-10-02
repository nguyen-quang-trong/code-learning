REM Viết chương trình giải phương trình bậc 2

set /p a=Nhap he so truoc x mu 2 (he so phai khac 0): 
if %a% EQU 0 Goto Error
set /p b=Nhap he so truoc x: 
set /p c=Nhap he so tu do: 
set /a delta=b*b - 4*a*c
if %delta% LSS 0 Goto VoNghiem
if %delta% EQU 0 Goto NghiemKep
set /a phanNguyenCanDelta=-1

:TimPhanNguyenCuaCanDelta
set /a phanNguyenCanDelta=%phanNguyenCanDelta%+1
set /a binhphuongPN=%phanNguyenCanDelta% * %phanNguyenCanDelta%
if %binhphuongPN% LSS %delta% Goto TimPhanNguyenCuaCanDelta
set /a canDelta=%phanNguyenCanDelta%
if %binhphuongPN% EQU %delta% Goto TinhNghiem
set /a phanNguyenCanDelta=%phanNguyenCanDelta%-1
set /a soCanSoSanh=(%delta% - %phanNguyenCanDelta% * %phanNguyenCanDelta%)*100
set soTimDuoc=%phanNguyenCanDelta%
set soChuSoPhanThapPhan=0

:TinhCanDelta
set x=-1

:TimXTrongBieuThuc
set /a x=%x%+1
set /a bieuthuc=(%soTimDuoc% * 20 + x)*x
if %soCanSoSanh% GTR %bieuthuc% Goto TimXTrongBieuThuc
if %soCanSoSanh% LSS %bieuthuc% set /a x=%x%-1

set /a bieuthuc=(%soTimDuoc% * 20 + x)*x
set /a soCanSoSanh= (%soCanSoSanh%-%bieuthuc%)*100
set soTimDuoc=%soTimDuoc%%x%
set /a soChuSoPhanThapPhan=%soChuSoPhanThapPhan%+1
if %soChuSoPhanThapPhan% EQU 3 Goto StopTinhCanDelta
if %soCanSoSanh% NEQ 0 Goto TinhCanDelta

:StopTinhCanDelta
set canDelta=%soTimDuoc%
set soChuSoKhong=0
set chuSoKhong=

:TimSoChuSoKhong
if %soChuSoKhong% EQU %soChuSoPhanThapPhan% Goto StopTimSoChuSoKhong
set /a soChuSoKhong=%soChuSoKhong%+1
set chuSoKhong=%chuSoKhong%0
Goto TimSoChuSoKhong

:StopTimSoChuSoKhong
set b=%b%%chuSoKhong%
set a=%a%%chuSoKhong%

:TinhNghiem
set /a x1= (-%b% + %canDelta%)/(2*%a%)
set /a sodu= (-%b% + %canDelta%) %% (2*%a%)
if %sodu% EQU 0 Goto TinhNghiemX2
if %x1% EQU 0 if %sodu% LSS 0 set x1=-%x1%
if %sodu% LSS 0 set sodu=%sodu% * (-1)
set /a sochia=2*%a%
set phanThapPhan=
set soChuSoPhanThapPhan=0
set vitri=2
Goto TinhPhanThapPhan
:vt2
set x1=%x1%.%phanThapPhan%

:TinhNGhiemX2
set /a x2= (-%b% - %canDelta%)/(2*%a%)
set /a sodu= (-%b% - %canDelta%) %% (2*%a%)
if %sodu% EQU 0 Goto StopTinhNgiem
if %x2% EQU 0 if %sodu% LSS 0 set x2=-%x2%
if %sodu% LSS 0 set sodu=%sodu% * (-1)
set /a sochia=2*%a%
set phanThapPhan=
set soChuSoPhanThapPhan=0
set vitri=3
Goto TinhPhanThapPhan
:vt3
set x2=%x2%.%phanThapPhan%

:StopTinhNgiem
echo Phuong trinh co hai ngiem phan biet: x1= %x1%; x2= %x2%
exit /b

:VoNghiem
echo Phuong trinh vo nghiem
exit /b

:NghiemKep
set /a x= (-%b%)/(2*%a%)
set /a sodu=(-%b%) %% (2*%a%)
if %sodu% EQU 0 Goto StopTinhNghiemKep
if %x% EQU 0 if %sodu% LSS 0 set x=-%x%
if %sodu% LSS 0 set sodu=%sodu%*(-1)
set /a sochia=2*%a%
set phanThapPhan=
set soChuSoPhanThapPhan=0
set vitri=1
Goto TinhPhanThapPhan
:vt1
set x=%x%.%phanThapPhan%

:StopTinhNghiemKep
echo Phuong trinh co nghiem kep x= %x%
exit /b

:TinhPhanThapPhan
set /a sobichia=%sodu% * 10
set /a thuong=%sobichia%/%sochia%
set phanThapPhan=%phanThapPhan%%thuong%
set /a sodu=%sobichia% %% %sochia%
set /a soChuSoPhanThapPhan=%soChuSoPhanThapPhan%+1
if %soChuSoPhanThapPhan% EQU 3 Goto StopTinhPhanThapPhan
if %sodu% NEQ 0 Goto TinhPhanThapPhan

:StopTinhPhanThapPhan
if %vitri% EQU 1 Goto vt1
if %vitri% EQU 2 Goto vt2
if %vitri% EQU 3 Goto vt3
exit /b

:Error
echo He so truoc x mu 2 khong hop le