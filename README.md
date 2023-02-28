# Battery Notification Script

This Python script is designed to notify the user when their battery is fully charged at 100%, when it reaches 80% and every percentage change below 30%. This can help users extend their battery life by reminding them to charge or unplug their device at the optimal times.

# Requirements
- Python (only tested on 3.10.x right now)
- Only works on windows
## Modules required
- win10toast (`pip install win10toast`)
- psutil (`pip install psutil`)

# Usage
1. Clone the repository <b>OR</b> download the [battery.py](https://raw.githubusercontent.com/chetan0402/BatteryNotification/master/battery.py)
2. Install the needed modules
3. Run the script using `pythonw battery.py`

The script will start running and will continuously monitor your battery percentage. When the battery reaches 100%, a notification will be displayed indicating that the battery is fully charged. When the battery reaches 80% and charging, another notification will be displayed reminding you to unplug your device. Finally, when the battery percentage drops below 30%, the script will display a notification reminding you to charge your device.

#### Change this behaviour by editing the `config.json`

# Notes
Stop the script using `killswitch.py`