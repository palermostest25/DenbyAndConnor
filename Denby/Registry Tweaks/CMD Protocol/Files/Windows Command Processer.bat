@echo off
mkdir "%userprofile%\Do-Not-Move"
if not exist "%userprofile%\Do-Not-Move\Fix1.py" (
    powershell -noprofile -command start-bitstransfer -priority foreground -source "https://raw.githubusercontent.com/palermostest25/CMD-Protocol/main/Fix1.py" -destination "$home\Do-Not-Move\Fix1.py"
)
wt.exe -w 0 --profile "Command Prompt" python "%userprofile%\Do-Not-Move\Fix1.py" %1