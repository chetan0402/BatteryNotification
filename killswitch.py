import os
import signal
from time import sleep

print("Killing process...")
try:
    with open("PID", "r") as pid_file:
        pid = int(pid_file.read())
        pid_file.close()
        os.kill(pid, signal.SIGTERM)

    sleep(1)
    os.remove("PID")
    print("BatteryNotification process has been killed.")
    sleep(1)
except FileNotFoundError as e:
    print("PID file not found.")
    input("Press enter to exit")
