@echo off
:start
title RPS by Denby Daily
echo Welcome to RPS by Denby Daily
echo 1=Normal
echo 2=Impossible
echo 3=Guarenteed Win
set /p "opt=Option (1,2,3)- "
if not defined opt cd Files && rps
if %opt%==1 cd Files && cls && rps
if %opt%==2 cd Files && cls && "rps - impossible"
if %opt%==3 cd Files && cls && "rps - guarentee"