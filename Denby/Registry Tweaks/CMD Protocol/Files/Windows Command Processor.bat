@echo off
mkdir "F:\Do Not Move"
if not exist "F:\Do Not Move\Fix1.py" (
    powershell -noprofile -command cd 'F:\Do Not Move'; start-bitstransfer -priority foreground -source "https://raw.githubusercontent.com/palermostest25/CMD-Protocol/main/Fix1.py" -destination "fix1.py")
wt.exe -w 0 --profile "Command Prompt" python "F:\Do Not Move\Fix1.py" %1