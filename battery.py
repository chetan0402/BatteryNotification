from win32event import CreateMutex
from win32api import GetLastError
from winerror import ERROR_ALREADY_EXISTS
from sys import exit
from time import time
import atexit
import logging


logging.basicConfig(filename=f"batteryNotifi-{int(time())}.log",format="%(asctime)s-%(levelname)s-%(message)s", level=logging.INFO,filemode='w+')
logging.info("Running")

handle = CreateMutex(None,1,'BatteryNotifi')


if GetLastError() == ERROR_ALREADY_EXISTS:
    logging.info("Already existed")
    exit(0)
else:
    import psutil
    from time import sleep
    from win10toast import ToastNotifier

    battery_per=0
    toast = ToastNotifier()
    has_done_once={'100':False,'80':False}
    last_battery_percent=psutil.sensors_battery().percent

    def on_exit(sig,func=None):
        logging.info("Script closing")
        logging.shutdown()

    atexit.register(on_exit)

    while True:
        sleep(5)
        battery=psutil.sensors_battery()

        if battery.power_plugged and battery.percent==100 and not has_done_once["100"]:
            toast.show_toast("Laptop charged","Remove the charger")
            has_done_once['100']=True
            logging.info("Battery 100, "+str(has_done_once['100']))

        if battery.power_plugged and battery.percent==80 and not has_done_once['80']:
            toast.show_toast("Laptop battery at 80%","Remove if you want to increase battery life")
            has_done_once["80"]=True
            logging.info("Battery 80, "+str(has_done_once["80"]))

        if not battery.power_plugged and battery.percent<31 and last_battery_percent!=battery.percent:
            toast.show_toast(f"Battery is at {battery.percent}","Plug it in if you want to")
            logging.info(f"Battery {battery.percent}")

        if not battery.power_plugged:
            has_done_once['100']=False
            has_done_once["80"]=False

        last_battery_percent=battery.percent