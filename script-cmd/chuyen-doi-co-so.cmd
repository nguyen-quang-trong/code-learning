REM Viết chương trình chuyển đổi một số từ cơ số n sang cơ số k

set /p a=Nhap so can chuyen: 
set /p n=Nhap co so cua so can chuyen:
set SoCanKiemTra=%a%
:KiemTraSuTonTaiCuaSoCanChuyen
set ChuSoCanKiemTra=%SoCanKiemTra:~-1%
if %ChuSoCanKiemTra% GEQ %n% Goto Error
set SoCanKiemTra=%SoCanKiemTra:~0,-1%
if "%SoCanKiemTra%" EQU "" Goto StopKiemTraSuTonTaiCuaSoCanChuyen
Goto KiemTraSuTonTaiCuaSoCanChuyen

:StopKiemTraSuTonTaiCuaSoCanChuyen
set /p k=Nhap co so can chuyen: 
if %k% EQU %n% echo Ket qua la %a%
if %k% EQU %n% exit /b
if %n% EQU 10 set kqcoso10=%a%
if %n% EQU 10 Goto StopTinhKetQuaCoSo10
set kqcoso10=0
set mu=1
set num=%a:~-1%
set a=%a:~0,-1%
set /a kqcoso10=%num%*%mu%
:TinhKetQuaCoSo10
if "%a%" EQU "" Goto StopTinhKetQuaCoSo10
set num=%a:~-1%
set a=%a:~0,-1%
set /a mu=%mu%*%n%
set /a kqcoso10=%num%*%mu%+%kqcoso10%
Goto TinhKetQuaCoSo10
:StopTinhKetQuaCoSo10
if %k% EQU 10 echo Ket qua la %kqcoso10%
if %k% EQU 10 exit /b
set /a thuong=%kqcoso10%/%k%
set /a sodu=%kqcoso10% %% %k%
set kq=%sodu%
:LOOP
if %thuong% EQU 0 Goto ENDL
set /a sodu=%thuong% %% %k%
set kq=%sodu%%kq%
set /a thuong=%thuong%/%k%
Goto LOOP
:ENDL
echo Ket qua la %kq%
exit /b
:Error
echo So can chuyen khong ton tai