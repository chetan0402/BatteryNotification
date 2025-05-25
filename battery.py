import psutil
try:
    with open("PID", "r+") as pid_file:
        pid = int(pid_file.read())
        process = psutil.Process(pid)
        if process.is_running() and process.name().find("python") != -1:
            print("BatteryNotifi is already running")
            exit(0)
except psutil.NoSuchProcess as e:
    print("BatteryNotifi is not running, starting a new instance")
    with open("PID", "w+") as pid_file:
        pid_file.write(str(psutil.Process().pid))
        pid_file.flush()
except Exception as e:
    exit(0)

from os import listdir, remove
from CustomLogger import Logger
import asyncio
from desktop_notifier import DesktopNotifier, common
import json
from time import sleep

logger = Logger()
logger.createFile()
logger.info("Running...")

notifier = DesktopNotifier()
last_battery_percent = psutil.sensors_battery().percent

try:
    with open('config.json') as json_file:
        config = json.load(json_file)
        json_file.close()
except json.JSONDecodeError as e:
    asyncio.run(notifier.send("BatteryNotification error", "Syntax Error in config file, check config.json", common.Urgency.Critical))
    exit(1)
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
    asyncio.run(notifier.send("BatteryNotification", "Config file created, edit config.json as per your needs", common.Urgency.Low))


def bool_(thing):
    return str(thing) in ["True","TRUE","1"]


if bool_(config["DEL_LOG"]):
    logger.deleteFile()
    for filename in listdir():
        if filename.startswith("batteryNotifi-") and filename.endswith(".log"):
            try:
                remove(filename)
            finally:
                pass


def send_battery_debug(battery):
    if not bool_(config["DEL_LOG"]):
        logger.info(f"Battery {battery.percent}")


def init_point():
    config["DONE_FULL_ONCE"] = False
    for points in config["point"]:
        points["DONE_ONCE"] = False


last_battery_percent = 0


def main_loop():
    sleep(1)
    battery = psutil.sensors_battery()
    global last_battery_percent
    global config

    if bool_(config["NOTIFY_WHEN_FULL"]) and battery.percent == 100 and not bool_(
            config["DONE_FULL_ONCE"]) and battery.power_plugged:
        asyncio.run(notifier.send("BatteryNotification", "Laptop battery at 100%, please remove from charging"))
        config["DONE_FULL_ONCE"] = True

    for points in config["point"]:
        if int(points["VAL"]) == battery.percent and not points["DONE_ONCE"] and battery.power_plugged == bool_(
                points["PLUG"]):
            asyncio.run(notifier.send(f"Laptop battery at {battery.percent}", points["MSG"]))
            points["DONE_ONCE"] = True
            last_battery_percent = battery.percent
            send_battery_debug(battery)

    for ranges in config["range"]:
        if int(ranges["MIN_VAL"]) <= battery.percent <= int(ranges[
            "MAX_VAL"]) and last_battery_percent != battery.percent and battery.power_plugged == bool_(
            ranges["PLUG"]):
            asyncio.run(notifier.send(f"Laptop battery at {battery.percent}", ranges["MSG"]))
            send_battery_debug(battery)

    if last_battery_percent != battery.percent:
        config["DONE_FULL_ONCE"] = False
        for points in config["point"]:
            points["DONE_ONCE"] = False
        last_battery_percent = battery.percent

    try:
        with open("battery.reload") as reload:
            with open('config.json') as json_file:
                config = json.load(json_file)
                json_file.close()
                init_point()
            reload.close()
        remove("battery.reload")
        send_battery_debug("Config reloaded")
    except FileNotFoundError:
        pass


init_point()
while True:
    main_loop()
