@echo off
:arguments
set 1=%1
if not defined 1 set 2=1
:prestart
if not exist %userprofile%\GetAverage.ps1 (
    powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/palermostest25/Get-Average/main/Get-Average.ps1 -OutFile $home\GetAverage.ps1"
    if errorlevel 1 echo Error When Downloading... && pause
)
set del=0
cd > tmpfile1
for /f "tokens=*" %%x in (tmpfile1) do (set curcd=%%x)
del tmpfile1
if defined var50 goto defined
if not defined 2 (
    set sum=%1% && goto after1
)
:start
set sum=0
set goto=0
title Calculator
cls
echo Welcome to the calculator
echo ==========V 5.0==========
echo PI
echo E
echo Pow
echo Sqrt
echo Square
echo Round
echo ABS
echo Avg for Average
echo DUnits for Data units
echo Conv for conversions
echo Cap for Cap or Not
set /p sum=Please enter your sum(Type ? for information)-
:after1
set sum=%sum: =%
set sum=%sum:,=%
set sum=%sum:x=*%
set sum=%sum:times=*%
set sum=%sum:divided=/%
set sum=%sum:by=%
set sum=%sum:plus=+%
set sum=%sum:minus=-%
call :replaceEqualSign in sum with -eq
echo.%sum%|findstr /C:"-eq" >nul 2>&1 && goto foundeq
:afterfoundeq
set sum=%sum:yourmum=9999999999999999999999999999999999999999999%
if %sum%==stevenhe echo EMOTIONAL DAMAGE & pause & goto start
if %sum%==emotionaldamage echo EMOTIONAL DAMAGE & pause & goto start
if %sum%==forza echo i like forza & pause & goto start
if %sum%==fortza echo thats not how you speel it :( & pause & goto start
set sum=%sum:pi=3.14159265358979%
set sum=%sum:e=2.71828182845905%
if %sum:~-1%==* set sum=%sum%2
if %sum%==cmd cmd
if %sum%==Cmd cmd
if %sum%==CMD cmd
if %sum%==cmdnew start cmd && exit
if %sum%==Cmdnew start cmd && exit
if %sum%==CmdNew start cmd && exit
if %sum%==CMDNEW start cmd && exit
if %sum%==cmd1 start cmd && exit
if %sum%==Cmd1 start cmd && exit
if %sum%==CMD1 start cmd && exit
if %sum%==powershell-noprofile powershell -noprofile
if %sum%==powershell-noprofile powershell -noprofile
if %sum%==powershell-noprofile powershell -noprofile
if %sum%==powershell-noprofile powershell -noprofile
if %sum%==powershell-noprofilenew start powershell -noprofile && exit
if %sum%==powershell-noprofilenew start powershell -noprofile && exit
if %sum%==powershell-noprofilenew start powershell -noprofile && exit
if %sum%==powershell-noprofileNew start powershell -noprofile && exit
if %sum%==powershell-noprofileNew start powershell -noprofile && exit
if %sum%==powershell-noprofileNEW start powershell -noprofile && exit
if %sum%==powershell-noprofile1 start powershell -noprofile && exit
if %sum%==powershell-noprofile1 start powershell -noprofile && exit
if %sum%==powershell-noprofile1 start powershell -noprofile && exit
if %sum%==POWWERSHELL1 start powershell -noprofile && exit
if %sum%==ps powershell -noprofile
if %sum%==Ps powershell -noprofile
if %sum%==PS powershell -noprofile
if %sum%==ps1 start powershell -noprofile && exit
if %sum%==Ps1 start powershell -noprofile && exit
if %sum%==PS1 start powershell -noprofile && exit
if %sum%==Psnew start powershell -noprofile && exit
if %sum%==psnew start powershell -noprofile && exit
if %sum%==PsNew start powershell -noprofile && exit
if %sum%==PSNEW start powershell -noprofile && exit
if %sum%==powershell start powershell && exit
if %sum%==Powershell start powershell && exit
if %sum%==PowerShell start powershell && exit
if %sum%==POWERSHELL start powershell&& exit
if %sum%==cap goto capornot
if %sum%==Cap goto capornot
if %sum%==CAP goto capornot
if %sum%==DUnits goto dunits
if %sum%==dunits goto dunits
if %sum%==Dunits goto dunits
if %sum%==dUnits goto dunits
if %sum%==DataUnits goto dunits
if %sum%==dataunits goto dunits
if %sum%==Dataunits goto dunits
if %sum%==dataUnits goto dunits
if %sum%==SquareRoot goto sqrt
if %sum%==Squareroot goto sqrt
if %sum%==squareRoot goto sqrt
if %sum%==squareroot goto sqrt
if %sum%==Sqrt goto sqrt
if %sum%==sqrt goto sqrt
if %sum%==SQRT goto sqrt
if %sum%==Round goto round
if %sum%==round goto round
if %sum%==R goto round
if %sum%==r goto round
if %sum%==ABS goto abs
if %sum%==Abs goto abs
if %sum%==abs goto abs
if %sum%==Absolute goto abs
if %sum%==Absolutevalue goto abs
if %sum%==absolute goto abs
if %sum%==absolutevalue goto abs
if %sum%==ABSOLUTEVALUE goto abs
if %sum%==ABSOLUTEVALUE goto abs
if %sum%==Pow goto pow
if %sum%==pow goto pow
if %sum%==POW goto pow
if %sum%==Power goto pow
if %sum%==power goto pow
if %sum%==POWER goto pow
if %sum%==Conv goto conv
if %sum%==conv goto conv
if %sum%==CONV goto conv
if %sum%==Conversion goto conv
if %sum%==CONVERSION goto conv
if %sum%==conversion goto conv
if %sum%==CONVERSIONS goto conv
if %sum%==Conversions goto conv
if %sum%==conversions goto conv
if %sum%==Square goto square
if %sum%==SQUARE goto square
if %sum%==square goto square
if %sum%==SquareNumber goto square
if %sum%==Squarenumber goto square
if %sum%==squarenumber goto square
if %sum%==squareNumber goto square
if %sum%==trans goto LNG
if %sum%==translate goto LNG
if %sum%==TRANS goto LNG
if %sum%==TRANSLATE goto LNG
if %sum%==LNG goto LNG
if %sum%==Translate goto LNG
if %sum%==Trans goto LNG
if %sum%==Lng goto LNG
if %sum%==lng goto LNG
if %sum%==LNG goto LNG
if %sum%==Lang goto LNG
if %sum%==LANG goto LNG
if %sum%==lang goto LNG
if %sum%==avg goto AVG
if %sum%==AVG goto AVG
if %sum%==Avg goto AVG
if %sum%==Average goto AVG
if %sum%==AVERAGE goto AVG
if %sum%==average goto AVG
if %sum%==Square goto square
if %sum%==SQUARE goto square
if %sum%==square goto square
set sum=%sum:x=*%
echo.%sum%|findstr /C:"pi" >nul 2>&1 && set goto=1
echo.%sum%|findstr /C:"e" >nul 2>&1 && set goto=1
if %goto%==1 goto calcsum1
if %sum%==? goto help

:calcsum1
powershell -noprofile %sum% > tmpfile
if %errorlevel%==1 cls && echo Error && if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
set /p awnser=<tmpfile
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
echo.%sum%|findstr /C:"3.14159265358979" >nul 2>&1 && set sum=%sum:3.14159265358979=PI%
echo.%sum%|findstr /C:"2.71828182845905" >nul 2>&1 && set sum=%sum:2.71828182845905=E%
cd %curcd%
echo %sum% = %awnser%
:end
echo Press any key to do another sum
pause > nul
goto start

:help
cls
echo + or = is addition
echo - is subtraction
echo * or x is multiplication
echo / is division
echo Use F7 to view history
echo Type anything that's above the prompt to get to that menu
pause
goto start

:dunits
echo KB
echo MB
echo GB
echo TB
echo PB
set /p dunits=Please enter the measurement-
if %dunits%==KB set dunits=KB
if %dunits%==kb set dunits=KB
if %dunits%==Kb set dunits=KB
if %dunits%==kB set dunits=KB
if %dunits%==K set dunits=KB
if %dunits%==k set dunits=KB

if %dunits%==MB set dunits=MB
if %dunits%==mb set dunits=MB
if %dunits%==Mb set dunits=MB
if %dunits%==mB set dunits=MB
if %dunits%==M set dunits=MB
if %dunits%==m set dunits=MB


if %dunits%==GB set dunits=GB
if %dunits%==gb set dunits=GB
if %dunits%==Gb set dunits=GB
if %dunits%==gB set dunits=GB
if %dunits%==G set dunits=GB
if %dunits%==g set dunits=GB

if %dunits%==TB set dunits=TB
if %dunits%==tb set dunits=TB
if %dunits%==Tb set dunits=TB
if %dunits%==tB set dunits=TB
if %dunits%==T set dunits=TB
if %dunits%==t set dunits=TB

if %dunits%==PB set dunits=PB
if %dunits%==pb set dunits=PB
if %dunits%==Pb set dunits=PB
if %dunits%==pB set dunits=PB
if %dunits%==P set dunits=PB
if %dunits%==p set dunits=PB

:calcdunits
echo 1
echo 2
echo 3
echo Etc.
set /p dunitsnum=What number of units would you like?-
powershell -noprofile %dunitsnum%%dunits% > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo %dunitsnum% %dunits% = %awnser% Bytes
pause
goto start


:sqrt
set sum=[Math]::Sqrt
set /p sqrtnum=What number would you like the Square root of?-
set sqrtnum1=(%sqrtnum%)
powershell -noprofile [Math]::Sqrt(%sqrtnum1%) > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo %sqrtnum% = %awnser%
echo Press any key to do another sum
pause > nul
goto start

:round
set sum=[Math]::Round
set /p roundnum=What number would you like to round?-
set roundnum1=%roundnum%
set roundnum1=%roundnum1:x=*%
set roundnum1=%roundnum1:pi=3.14159265358979%
set roundnum1=%roundnum1:e=2.71828182845905%
echo.%roundnum1%|findstr /C:"*" >nul 2>&1 && goto roundcalc
echo.%roundnum1%|findstr /C:"+" >nul 2>&1 && goto roundcalc
echo.%roundnum1%|findstr /C:"/" >nul 2>&1 && goto roundcalc
echo.%roundnum1%|findstr /C:"-" >nul 2>&1 && goto roundcalc
:round1
set roundnum1=%roundnum1:3.14159265358979=PI%
set roundnum1=%roundnum1:2.71828182845905=E%
set /p amountofdecimals=How many decimal places would you like to round %roundnum1% to?-
set roundnum1=%roundnum1:pi=3.14159265358979%
set roundnum1=%roundnum1:e=2.71828182845905%
powershell -noprofile %sum%(%roundnum1%,%amountofdecimals%) > tmpfile
set roundnum1=%roundnum1:3.14159265358979=PI%
set roundnum1=%roundnum1:2.71828182845905=E%
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo %roundnum1% rounded to %amountofdecimals% decimal places = %awnser%
echo Press any key to do another sum
pause > nul
goto start

:round2
set sum=[Math]::Round
set roundnum=%roundavgawn%
set roundnum1=%roundnum%
set roundnum1=%roundnum1:x=*%
set roundnum1=%roundnum1:pi=3.14159265358979%
set roundnum1=%roundnum1:e=2.71828182845905%
echo.%roundnum1%|findstr /C:"*" >nul 2>&1 && goto roundcalc1
echo.%roundnum1%|findstr /C:"+" >nul 2>&1 && goto roundcalc1
echo.%roundnum1%|findstr /C:"/" >nul 2>&1 && goto roundcalc1
echo.%roundnum1%|findstr /C:"-" >nul 2>&1 && goto roundcalc1
:round3
set roundnum1=%roundnum1:3.14159265358979=PI%
set roundnum1=%roundnum1:2.71828182845905=E%
if defined roundavgnum set amountofdecimals=2
if defined roundavgnum goto afteramntofdecimalsround2
set /p amountofdecimals=How many decimal places would you like to round %roundnum1% to?-
:afteramntofdecimalsround2
set roundnum1=%roundnum1:pi=3.14159265358979%
set roundnum1=%roundnum1:e=2.71828182845905%
powershell -noprofile %sum%(%roundnum1%,%amountofdecimals%) > tmpfile
set roundnum1=%roundnum1:3.14159265358979=PI%
set roundnum1=%roundnum1:2.71828182845905=E%
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo %roundnum1% rounded to %amountofdecimals% decimal places = %awnser%
echo Press any key to do another sum
pause > nul
goto start

:AVG
set /p "num=Enter the numbers you would like to average. eg. 1,2,3,4- "
echo The Average of %num% is
powershell cd $home; "GetAverage.ps1" %num%
echo Press any key to do another sum
pause > nul
goto start

:abs
set /p absvalue=What number would you like to find the absolute value of?-
set sum=[Math]::Abs
powershell -noprofile %sum%(%absvalue%) > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo The absolute value of %absvalue% is %awnser%
echo Press any key to do another sum
pause > nul
goto start



:pow
set /p pow=What number would you like?-
set /p powto=To the power of-
set sum=[Math]::Pow
powershell -noprofile %sum%(%pow%,%powto%) > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo %pow% to the power of %powto% is %awnser%
echo Press any key to do another sum
pause > nul
goto start




:square
set /p sqr=What number would you like to find the square of?-
powershell -noprofile %sqr% * %sqr% > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo The square of %sqr% is %awnser%
echo Press any key to do another sum
pause > nul
goto start


:conv
echo 1=Miles to KM
echo 2=Pounds to KG
echo 3=Celsius to Fahrenheit
echo 4=Fractions to Decimals
echo 5=Percentages to Fractions
echo 6=Percentages to Decimals
echo 7=Percent of a number
echo 8=Percent off
echo 9=Inches to CM
echo 10=GST Calculator
echo 11=Add percent to a number
echo 12=Language Translation jk Google Translate
echo 13=Month Information
echo 14=What percentage of a number is in a number

set /p convopt=What option would you like(1,2,3,4,5,6,7,8,9,10,11,12,13,14)-
if %convopt%==1 goto MKM
if %convopt%==2 goto PKG
if %convopt%==3 goto CTF 
if %convopt%==4 goto FTD
if %convopt%==5 goto PTF
if %convopt%==6 goto PTD
if %convopt%==7 goto PON
if %convopt%==8 goto PCO
if %convopt%==9 goto ITC
if %convopt%==10 goto GST
if %convopt%==11 goto APS
if %convopt%==12 goto LNG
if %convopt%==13 goto MNT
if %convopt%==14 goto PNN
if %convopt%==gst goto GST
if %convopt%==Gst goto GST
if %convopt%==GST goto GST





:MKM
echo 1=Miles to KM
echo 2=KM to Miles
set /p milesorkm=Would you like to go from Miles to KM or KM to Miles?-
if %milesorkm%==1 goto milesfirst
if %milesorkm%==2 goto kmfirst

:milesfirst
set /p miles=Miles-
powershell -noprofile %miles% * 1.609 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
if %miles%==1 set milesormile=Mile
if not %miles%==1 set milesormile=Miles
cd %curcd%
echo %miles% %milesormile% is %awnser% KM
echo Press any key to do another sum
pause > nul
goto start


:kmfirst
set /p km=Kilometers-
powershell -noprofile %km% / 1.609 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo %km% KM is %awnser% Miles
echo Press any key to do another sum
pause > nul
goto start

:PKG
echo 1=Pounds to KG
echo 2=KG to Pounds
set /p poundkg=What option would you like?-
if %poundkg%==1 goto pfirst
if %poundkg%==2 goto kfirst


:pfirst
set /p pounds=Pounds-
powershell -noprofile %pounds% / 2.205 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
if %pounds%==1 set poundsorpound=Pound
if not %pounds%==1 set poundsorpound=Pounds
cd %curcd%
echo %pounds% %poundsorpound% is %awnser% KG
echo Press any key to do another sum
pause > nul
goto start

:kfirst
set /p kg=KG-
powershell -noprofile %kg% * 2.205 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo %kg% KG is %awnser% Pounds
echo Press any key to do another sum
pause > nul
goto start


:CTF
echo 1=Celsius to Fahrenheit
echo 2=Farenheit to Celsius
set /p ctfopt=What option would you like?-
if %ctfopt%==1 goto cfirst
if %ctfopt%==2 goto ffirst


:cfirst
set /p c=Celsius-
powershell -noprofile (%c%*9/5)+32 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul


set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
if %c%==1 set degreeordegrees=Degree
if not %c%==1 set degreeordegrees=Degrees
if %awnser%==1 set degreeordegrees2=Degree
if not %awnser%==1 set degreeordegrees2=Degrees
cd %curcd%
echo %c% %degreeordegrees% Celsius is %awnser% %degreeordegrees2% Farenheit
echo Press any key to do another sum
pause > nul
goto start

:ffirst
set /p f=Farenheit-
powershell -noprofile (%f-%32)*5/9 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
if %f%==1 set fdegreeordegrees=Degree
if not %f%==1 set fdegreeordegrees=Degrees
if %awnser%==1 set fdegreeordegrees2=Degree
if not %awnser%==1 set fdegreeordegrees2=Degrees
echo %f% Degrees Farenheit is %awnser% %fdegreeordegrees2% Celsius
cd %curcd%
echo Press any key to do another sum
pause > nul
goto start

:FTD
echo A calculator cannot go from decimal to fraction :(
set /p nume=Numerator-
set /p deno=Denominator-

powershell -noprofile %nume% / %deno% > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser= < tmpfile
if exist tmpfile del /q tmpfile > nul


set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
echo / Means the line in the middle of a fraction (Vinculum)
echo %nume% / %deno% = %awnser%
cd %curcd%
echo Press any key to do another sum
pause > nul
goto start



:PTF
echo A calculator cannot go from fractions to percentages :(
set /p percentage=Percentage(No Percentage Sign)-
set deno=100
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
echo / Means the line in the middle of a fraction (Vinculum)
echo %percentage% Percent as a fraction = %percentage% / %deno%
cd %curcd%
echo Press any key to do another sum
pause > nul
goto start



:PTD
echo 1=Percentages to Decimals
echo 2=Decimals to Percentages
set /p ptdopt=What option would you like?-
if %ptdopt%==1 goto PTDPFirst
if %ptdopt%==2 goto PTDDFirst


:PTDPFirst
set /p percentage=Percentage(No Percentage Sign)-
powershell -noprofile %percentage% / 100 > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser= < tmpfile
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
echo %percentage% Percent = %awnser%
cd %curcd%
echo Press any key to do another sum
pause > nul
goto start


:PTDDFirst
set /p decimal=Decimal(With a 0. at the start)-
powershell -noprofile %decimal% * 100 > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser= < tmpfile
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
echo %decimal% = %awnser% Percent
cd %curcd%
echo Press any key to do another sum
pause > nul
goto start




:PON
set /p percent=Percentage(No percentage sign)-
set /p numberpon=Number to find the percent of-
powershell -noprofile %percent% / 100 > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser1= < tmpfile
if exist tmpfile del /q tmpfile > nul
powershell -noprofile %awnser1% * %numberpon% > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser= < tmpfile
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
echo %percent% Percent of %numberpon% = %awnser%
cd %curcd%
echo Press any key to do another sum
pause > nul
goto start


:PCO
set /p numberpco=Origional Price(No dollar sign)-
set /p percent=Percentage off(No percentage sign)-
powershell -noprofile %percent% / 100 > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser1= < tmpfile
if exist tmpfile del /q tmpfile > nul
powershell -noprofile %awnser1% * %numberpco% > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser2= < tmpfile
if exist tmpfile del /q tmpfile > nul
powershell -noprofile %numberpco% - %awnser2% > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser= < tmpfile
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
echo You save $%awnser2%
echo %percent% Percent off $%numberpco% = $%awnser%
cd %curcd%
echo Press any key to do another sum
pause > nul
goto start

:ITC
echo 1=Inches to CM
echo 2=CM to Inches
set /p inchesorcm=Would you like to go from Inches to CM or CM to Inches?-
if %inchesorcm%==1 goto inchesfirst
if %inchesorcm%==2 goto cmfirst

:inchesfirst
set /p inches=Inches-
powershell -noprofile %inches% * 2.54 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
if %inches%==1 set inchesorinch=Inch
if not %inches%==1 set inchesorinch=Inches
cd %curcd%
echo %inches% %inchesorinch% is %awnser% CM
echo Press any key to do another sum
pause > nul
goto start

:cmfirst
set /p cm=CM-
powershell -noprofile %cm% / 2.54 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
if %awnser%==1 set inchesorinch=Inch
if not %awnser%==1 set inchesorinch=Inches
cd %curcd%
echo %cm% CM is %awnser% %inchesorinch%
echo Press any key to do another sum
pause > nul
goto start



:GST
echo 1=Before
echo 2=After
set /p gstopt=Would you like to calculate GST from a price without before or after GST?(1,2)-
if %gstopt%==1 goto beforegst
if %gstopt%==2 goto aftergst


:beforegst
set /p origprice=Origional Price(No dollar sign)-
powershell -noprofile %origprice% * 1.1 > tmpfile
set /p awnser= < tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
if exist tmpfile del /q tmpfile > nul
powershell -noprofile %awnser% / 11 > tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
set /p gst= < tmpfile
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo $%origprice% + $%gst% GST = $%awnser%
echo Press any key to do another sum
pause > nul
goto start


:aftergst
set /p priceaftergst=Price After GST(No dollar sign)-
powershell -noprofile %priceaftergst% / 11 > tmpfile
if %errorlevel%==1 cls && echo Error && if del==0 if exist tmpfile del /q tmpfile > nul && pause && cls && goto start
set /p gst= < tmpfile
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
echo The GST of $%priceaftergst% = $%gst%
echo Press any key to do another sum
pause > nul
goto start

:APS
set /p percent=Percentage(No percentage sign)-
set /p numberaps=Number to add percent to-
powershell -noprofile %percent% / 100 > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser1= < tmpfile
if exist tmpfile del /q tmpfile > nul
powershell -noprofile %awnser1% * %numberaps% > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser2= < tmpfile
if exist tmpfile del /q tmpfile > nul
powershell -noprofile %awnser2% + %numberaps% > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser= < tmpfile
if exist tmpfile del /q tmpfile > nul
set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
echo %numberaps% + %percent% Percent = %awnser% Total
cd %curcd%
echo Press any key to do another sum
pause > nul
goto start

:LNG
start /max https://translate.google.com
echo Do you really think I was going to code that?
echo Press any key to go back to the start
pause > nul
goto start

:MNT
echo Month Data:
echo Number - Month - Short Form - Days
echo 1 - January - Jan - 31
echo 2 - Feburary - Feb - 28/29
echo 3 - March - Mar - 31
echo 4 - April - Apr - 30
echo 5 - May - May - 31
echo 6 - June - Jun - 30
echo 7 - July - Jul - 31
echo 8 - August - Aug - 31
echo 9 - September - Sep - 30
echo 10 - October - Oct - 31
echo 11 - November - Nov - 30
echo 12 - December - Dec - 31
echo Press any key to go back to the start
pause > nul
cls
goto start

:PNN
set /p num1=Fractioned number-
set /p num2=Total number-
powershell -noprofile %num1% / %num2% * 100 > tmpfile
if %errorlevel%==1 cls && echo Error && del /q tmpfile && pause && cls && goto start
set /p awnser= < tmpfile
if exist tmpfile del /q tmpfile > nul
echo %num1% is %awnser% percent of %num2%
echo Press any key to do another sum
pause > nul
goto start

:roundcalc
powershell -noprofile %roundnum1% > tmpfile
set /p awnser=<tmpfile
if exist tmpfile del /q tmpfile > nul


set date1=%date:/=_%
set date1=%date1: =_%
set time1=%time::=.%
cd %curcd%
goto round1

:capornot
echo Welcome to Cap or Not
echo You will be given a maths sum and you need to awnser whether is is cap or not.
:generaterandomnumberforcapornot
powershell -noprofile get-random -min 1 -max 1000 > num1
set /p num1=<num1
del num1
:guess
set /p "guess=Guess the Number- "
set /a guessnum=%guess%
if %guessnum% gtr %num1% (
    echo Lower!
    goto guess
)
if %guessnum% lss %num1% (
    echo Higher!
    goto guess
)
if %guessnum%==%num1% (
    echo Good Job!
    echo Press Any Key to Go Back to The Start...
    pause > nul
    goto start
)
:replaceEqualSign in sum with  -eq 
    setlocal enableDelayedExpansion

        set "_s=!%~2!#"
        set "_r="

        :_replaceEqualSign
            for /F "tokens=1* delims==" %%A in ("%_s%") do (
                if not defined _r ( set "_r=%%A" ) else ( set "_r=%_r%%~4%%A" )
                set "_s=%%B"
            )
        if defined _s goto _replaceEqualSign

    endlocal&set "%~2=%_r:~0,-1%"
exit /b
:foundeq
powershell -noprofile $sum = "%sum%"; if ($sum) {write-output True}else {write-output False}
:end
echo Press any key to do another sum
pause > nul
goto start
exit /B

















