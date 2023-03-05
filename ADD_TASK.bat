@setlocal enableextensions
@cd /d "%~dp0"
echo ^<?xml version="1.0" encoding="UTF-16"?^>^<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task"^>^<RegistrationInfo^>^<Date^>2023-03-04T23:00:22.7870839^</Date^>^<Author^>LAPTOP-KN3MBJH3\\ASUS BOOK^</Author^>^<URI^>\\BatteryNotification^</URI^>^</RegistrationInfo^>^<Triggers^>^<LogonTrigger^>^<Enabled^>true^</Enabled^>^</LogonTrigger^>^</Triggers^>^<Principals^>^<Principal id="Author"^>^<UserId^>S-1-5-21-184439906-1599863775-4260581706-1003^</UserId^>^<LogonType^>InteractiveToken^</LogonType^>^<RunLevel^>LeastPrivilege^</RunLevel^>^</Principal^>^</Principals^>^<Settings^>^<MultipleInstancesPolicy^>IgnoreNew^</MultipleInstancesPolicy^>^<DisallowStartIfOnBatteries^>false^</DisallowStartIfOnBatteries^>^<StopIfGoingOnBatteries^>false^</StopIfGoingOnBatteries^>^<AllowHardTerminate^>true^</AllowHardTerminate^>^<StartWhenAvailable^>false^</StartWhenAvailable^>^<RunOnlyIfNetworkAvailable^>false^</RunOnlyIfNetworkAvailable^>^<IdleSettings^>^<StopOnIdleEnd^>true^</StopOnIdleEnd^>^<RestartOnIdle^>false^</RestartOnIdle^>^</IdleSettings^>^<AllowStartOnDemand^>true^</AllowStartOnDemand^>^<Enabled^>true^</Enabled^>^<Hidden^>false^</Hidden^>^<RunOnlyIfIdle^>false^</RunOnlyIfIdle^>^<DisallowStartOnRemoteAppSession^>false^</DisallowStartOnRemoteAppSession^>^<UseUnifiedSchedulingEngine^>true^</UseUnifiedSchedulingEngine^>^<WakeToRun^>false^</WakeToRun^>^<ExecutionTimeLimit^>PT72H^</ExecutionTimeLimit^>^<Priority^>7^</Priority^>^</Settings^>^<Actions Context="Author"^>^<Exec^>^<Command^>%cd%\RUN_IN_BACKGROUND_NO_WAIT.bat^</Command^>^</Exec^>^</Actions^>^</Task^> >> "BATTERY_TASK.xml"
schtasks /create /tn "BatteryNotification" /xml BATTERY_TASK.xml
del BATTERY_TASK.xml