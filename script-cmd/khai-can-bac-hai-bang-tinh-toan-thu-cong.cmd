Echo off
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
Set /a SoTimDuoc=%i%
Set /a SoCanSoSanh=(%SoCanKhaiCan% - %SoTimDuoc% * %SoTimDuoc%) * 100
Set /p SoChuSoThapPhan=Nhap so chu so thap phan ban can (tu 1 den 4): 
if %SoChuSoThapPhan% LSS 1 Goto ERROR2
if %SoChuSoThapPhan% GTR 4 Goto ERROR2

Set /a i=1
:WHILE2
    Set /a j=0
    :WHILE3
        Set /a BieuThuc=(%SoTimDuoc%*20 + %j%) * %j%
        if %BieuThuc% GTR %SoCanSoSanh% Goto ENDW3
        Set /a j=%j%+1
        Goto WHILE3
    :ENDW3
        Set /a j=%j% - 1
        Set /a SoCanSoSanh=(%SoCanSoSanh% - ((%SoTimDuoc%*20 + %j%) * %j%)) * 100
        Set /a SoTimDuoc=%SoTimDuoc% * 10 + %j%
        Set kq=%kq%%j%
    Set /a i=%i%+1
    if %i% LEQ %SoChuSoThapPhan% Goto WHILE2
:KQ
    Echo Can bac hai cua %SoCanKhaiCan% la %kq%
    Exit /b
:ERROR1
    Echo Khong duoc phep nhap so am
    Exit /b
:ERROR2
    Echo So chu so thap phan khong hop le