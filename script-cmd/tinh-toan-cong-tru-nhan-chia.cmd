set /p a=Nhap a= 
set /p b=Nhap b (b!=0) = 
if %b% EQU 0 Goto Error

:TimDauPhayVaThayDauPhayThanhDauCham
set a=%a:,=.%
set b=%b:,=.%

call :DemSoChuSoThapPhan %a% soChuSoThapPhanCuaA
call :DemSoChuSoThapPhan %b% soChuSoThapPhanCuaB

:ChuanHoaPhanThapPhanCuaA&B
if %soChuSoThapPhanCuaA% EQU %soChuSoThapPhanCuaB% Goto KhuDauThapPhan
if %soChuSoThapPhanCuaA% LSS %soChuSoThapPhanCuaB% Goto ThemSoKhongChoA
set b=%b%0
set /a soChuSoThapPhanCuaB=%soChuSoThapPhanCuaB%+1
Goto ChuanHoaPhanThapPhanCuaA&B

:ThemSoKhongChoA
set a=%a%0
set /a soChuSoThapPhanCuaA=%soChuSoThapPhanCuaA%+1
Goto ChuanHoaPhanThapPhanCuaA&B

:KhuDauThapPhan
set a=%a:.=%
set b=%b:.=%

set /a tong=%a% + %b%
set /a hieu=%a% - %b%
set /a tich=%a% * %b%
if %tong% NEQ 0 call :ChuanHoaKetQua %soChuSoThapPhanCuaA% %tong% tong
if %hieu% NEQ 0 call :ChuanHoaKetQua %soChuSoThapPhanCuaA% %hieu% hieu
set soChuSoThapPhanCuaTich=%soChuSoThapPhanCuaA%+%soChuSoThapPhanCuaB%
if %tich% NEQ 0 call :ChuanHoaKetQua %soChuSoThapPhanCuaTich% %tich% tich

set /a PhanNguyenCuaThuong=%a% / %b%
set /a sodu=(%a% %% %b%)*10
if %b% LSS 0 set /a b=%b% * (-1)
if %sodu% LSS 0 set /a sodu=%sodu% * (-1)
set soChuSoThapPhanCuaThuong=0
set PhanThapPhanCuaThuong=
:TimPhanThapPhanCuaThuong
set /a thuong=%sodu% / %b%
set PhanThapPhanCuaThuong=%PhanThapPhanCuaThuong%%thuong%
set /a sodu=(%sodu% %% %b%) * 10
set /a soChuSoThapPhanCuaThuong=%soChuSoThapPhanCuaThuong%+1
if %soChuSoThapPhanCuaThuong% EQU 8 Goto StopTimPhanThapPhanCuaThuong
if %sodu% NEQ 0 Goto TimPhanThapPhanCuaThuong
:StopTimPhanThapPhanCuaThuong
set DauCuaTich=%tich:~0,1%
set thuong=%PhanNguyenCuaThuong%.%PhanThapPhanCuaThuong%
if %PhanNguyenCuaThuong% EQU 0 if "%DauCuaTich%" EQU "-" set thuong=-%thuong%

echo tong=%tong%
echo hieu=%hieu%
echo tich=%tich%
echo thuong=%thuong%
exit /b

:DemSoChuSoThapPhan
set str=%1
set soChuSoThapPhan=0
:LapDemSoChuSoThapPhan
set kt=%str:~-1%
if "%kt%" EQU "." Goto StopLapDemSoChuSoThapPhan
set /a soChuSoThapPhan=%soChuSoThapPhan%+1
set str=%str:~0,-1%
Goto LapDemSoChuSoThapPhan
:StopLapDemSoChuSoThapPhan
set %2=%soChuSoThapPhan%
exit /b

:ChuanHoaKetQua
set soChuSoThapPhan=%1
set PhanNguyen=%2
set PhanThapPhan=
set ktDauKQ=%PhanNguyen:~0,1%
if "%ktDauKQ%" EQU "-" set /a PhanNguyen=%PhanNguyen% * (-1)
:TimPhanThapPhan
if %soChuSoThapPhan% EQU 0 Goto StopTimPhanThapPhan
set PhanThapPhan=%PhanNguyen:~-1%%PhanThapPhan%
set PhanNguyen=%PhanNguyen:~0,-1%
set /a soChuSoThapPhan=%soChuSoThapPhan%-1
if "%PhanNguyen%" EQU "" set PhanNguyen=0
Goto TimPhanThapPhan
:StopTimPhanThapPhan
set kq=%PhanNguyen%.%PhanThapPhan%
if "%ktDauKQ%" EQU "-" set kq=-%kq%
set %3=%kq%
exit /b

:Error
echo Gia tri cua b phai khac 0