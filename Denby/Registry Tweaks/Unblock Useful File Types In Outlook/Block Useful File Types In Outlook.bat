@echo off
title Outlook File Type Unblocker
echo Unblocking Outlook Useful File Types
echo Y | reg delete HKEY_CURRENT_USER\SOFTWARE\Microsoft\Office\16.0\Outlook\Security /v Level1Remove
echo Success!
echo Press any key to exit
pause > nul
exit /B