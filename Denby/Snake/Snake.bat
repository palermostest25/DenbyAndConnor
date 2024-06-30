@echo off
title Snake
:start
python --version 3 > NUL
if errorlevel 1 goto errorNoPython

pip install pygame
echo 0 > randomfile.txt
attrib -s +- "randomfile.txt"
cls
python snake.py
goto eof

:errorNoPython
echo Python Is Not Installed
python
pause
goto start

:eof
exit