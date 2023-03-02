import os
import signal
from time import sleep
import psutil

print("Killing process...")
try:
    with open("PID", "r") as pid_file:
        pid = int(pid_file.read())
        pid_file.close()

    try:
        process_python = psutil.Process(pid)
        if "py" in process_python.name():
            os.kill(pid, signal.SIGTERM)
            sleep(1)
            os.remove("PID")
            print("BatteryNotification process has been killed.")
            sleep(1)
        else:
            os.remove("PID")
            print("BatteryNotification process not running already.")
            sleep(1)
    except psutil.NoSuchProcess:
        os.remove("PID")
        print("BatteryNotification process not running already.")
        sleep(1)
except FileNotFoundError:
    print("PID file not found.")
    input("Press enter to exit")
