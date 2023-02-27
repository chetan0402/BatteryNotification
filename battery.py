from win32event import CreateMutex
from win32api import GetLastError
from winerror import ERROR_ALREADY_EXISTS
from sys import exit
from time import time
import logging
from os import remove

filename = f"batteryNotifi-{int(time())}.log"
logging.basicConfig(filename=filename, format="%(asctime)s-%(levelname)s-%(message)s", level=logging.INFO,
                    filemode='w+')
logging.info("Running")

handle = CreateMutex(None, 1, 'BatteryNotifi')

if GetLastError() == ERROR_ALREADY_EXISTS:
    logging.info("Already existed")
    exit(0)
else:
    import psutil
    from time import sleep
    from win10toast import ToastNotifier
    import json

    toast = ToastNotifier()
    last_battery_percent = psutil.sensors_battery().percent

    try:
        with open('config.json') as json_file:
            config = json.load(json_file)
            json_file.close()
    except ValueError as e:
        toast.show_toast("Syntax Error in config file", "Check config.json")
    except FileNotFoundError as e:
        config_default = """{
            "range":[
                {"MAX_VAL":30,"MIN_VAL":0,"MSG":"Put laptop in charging","PLUG":"False"}
                ],
            "point":[
                {"VAL":80,"MSG":"Remove from charging","PLUG":"True"}
                ],
            "NOTIFY_WHEN_FULL":"True",
            "DEL_LOG":"True"
            }"""
        with open('config.json', "rw+") as json_file:
            json_file.write(config_default)
            config = json.load(json_file)
            json_file.close()
        toast.show_toast("Config file created", "Edit config.json as per your needs")


    def bool_(thing):
        if str(thing) == "True" or str(thing) == "TRUE" or str(thing) == "1":
            return True
        else:
            return False


    if bool_(config["DEL_LOG"]):
        logging.disable()
        remove(filename)  # doesn't work currently


    def send_battery_debug(battery):
        if not bool_(config["DEL_LOG"]):
            logging.info(f"Battery {battery.percent}")


    def init_point():
        config["DONE_FULL_ONCE"] = False
        for points in config["point"]:
            points["DONE_ONCE"] = False


    last_battery_percent = 0


    def main_loop():
        sleep(1)
        battery = psutil.sensors_battery()
        global last_battery_percent

        if bool_(config["NOTIFY_WHEN_FULL"]) and battery.percent == 100 and not bool_(
                config["DONE_FULL_ONCE"]) and not battery.power_plugged:
            toast.show_toast("Laptop abttery at 100%", "Please remove from charging")
            config["DONE_FULL_ONCE"] = True

        for points in config["point"]:
            if points["VAL"] == battery.percent and not points["DONE_ONCE"] and battery.power_plugged == bool_(
                    config["PLUG"]):
                toast.show_toast(f"Laptop battery at {battery.percent}", points["MSG"])
                points["DONE_ONCE"] = True
                send_battery_debug(battery)

        for ranges in config["range"]:
            if ranges["MIN_VAL"] <= battery.percent <= ranges[
                "MAX_VAL"] and last_battery_percent != battery.percent and battery.power_plugged == bool_(ranges["PLUG"]):
                toast.show_toast(f"Laptop battery at {battery.percent}", ranges["MSG"])
                send_battery_debug(battery)

        if last_battery_percent != battery.percent:
            config["DONE_FULL_ONCE"] = False
            for points in config["point"]:
                points["DONE_ONCE"] = False
            last_battery_percent = battery.percent


    init_point()
    while True:
        main_loop()
