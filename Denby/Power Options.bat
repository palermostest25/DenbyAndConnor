@echo off

title Power Options
:start
ECHO ==========V 1.0==========
ECHO Choose an option
ECHO 1 = Logoff
ECHO 2 = Reboot
ECHO 3 = Hibernate
ECHO 4 = Shutdown
ECHO For Advanced Options Type "?"
ECHO To Abort Timed Shutdown Type Stop Into The "Choose An Option" Section

SET /p option=Choose one option-
IF %option%==stop shutdown /a 
IF %option%==1 shutdown /l
IF %option%==Stop shutdown /a
IF %option%==STOP shutdown /a 
IF %time%==stop shutdown /a 
IF %time%==Stop shutdown /a 
IF %time%==STOP shutdown /a 
IF %option%==? goto qna
SET /p time=Time before taking action in seconds(Cannot Use Lock And Timer)-


IF %option%==1 shutdown /l
IF %option%==2 SHUTDOWN -r /t %time%
IF %option%==3 SHUTDOWN /h /t %time%
IF %option%==4 SHUTDOWN /s /t %time% /hybrid

exit
:qna
cls
title Help Screen
ECHO Welcome to the help page for the Power Options Program
ECHO Syntax=Power Option (1,2,3 or 4)
ECHO Then Time in seconds
ECHO HELPFUL HINTS
ECHO 30 Minutes = 1800 Seconds
ECHO 1 Hour = 3600 Seconds
ECHO 2 Hours = 7200 Seconds
ECHO 4 Hours = 14400 Seconds
ECHO 10 Hours = 36000 Seconds
pause
exit




