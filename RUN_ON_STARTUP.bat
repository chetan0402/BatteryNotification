@setlocal enableextensions
@cd /d "%~dp0"
@echo off
powershell "$s=(New-Object -COM WScript.Shell).CreateShortcut('%userprofile%\Start Menu\Programs\Startup\BatteryNotification.lnk');$s.TargetPath='%cd%/RUN_IN_BACKGROUND_NO_WAIT.bat';$s.WorkingDirectory='%cd%';$s.Save()"
echo Battery Notification will now run on startup
pause