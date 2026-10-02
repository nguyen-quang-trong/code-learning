REM Viết chương trình khai căn bậc hai, dùng giải thuật tìm kiếm tuyến tính.

Set /p SoCanKhaiCan=Nhap so can khai can: 
if %SoCanKhaiCan% LSS 0 Goto ERROR1
Set /a kq=0

Set /a i=0
:WHILE1
    Set /a max=%i% * %i%
    if %max% EQU %SoCanKhaiCan% Goto ENDW1.0
    if %max% GTR %SoCanKhaiCan% Goto ENDW1.1
    Set /a i=%i%+1
    Goto WHILE1
:ENDW1.0
    Set /a kq=%i%
    Goto KQ
:ENDW1.1
Set /a i=%i%-1
Set kq=%i%.
Set /p SoChuSoThapPhan=Nhap so chu so thap phan ban can (tu 1 den 4): 
if %SoChuSoThapPhan% LSS 1 Goto ERROR2
if %SoChuSoThapPhan% GTR 4 Goto ERROR2
Set ChuSoKhong=

Set /a j=0
:FOR
    if %j% GEQ %SoChuSoThapPhan% Goto ENDF
    Set ChuSoKhong=%ChuSoKhong%0
    Set /a j=%j% + 1
    Goto FOR
:ENDF

Set i=%i%%ChuSoKhong%
Set SoCanSoSanh=%SoCanKhaiCan%%ChuSoKhong%%ChuSoKhong%
:WHILE2
    Set /a max=%i% * %i%
    if %max% GTR %SoCanSoSanh% Goto ENDW2
    Set /a i=%i%+1
    Goto WHILE2
:ENDW2
Set /a i=%i%-1
Set PhanThapPhan=

Set /a j=0
:WHILE3
    Set /a Num=%i% %% 10
    Set PhanThapPhan=%Num%%PhanThapPhan%
    Set i=%i:~0,-1%
    Set /a j=%j% + 1
    if %j% LSS %SoChuSoThapPhan% Goto WHILE3
    Set kq=%kq%%PhanThapPhan%
:KQ
    Echo Can bac hai cua %SoCanKhaiCan% la %kq%
    Exit /b
:ERROR1
    Echo Khong duoc phep nhap so am
    Exit /b
:ERROR2
    Echo So chu so thap phan khong hop le