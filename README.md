# Battery Notification Script

This Python script is designed to notify the user when their battery is various levels. This can help users extend their battery life by reminding them to charge or unplug their device at the optimal times. (Set the percentage on when to notify by editing the `config.json` using `ConfigBuilder.html`)

# Requirements
- Python
## Modules required
- Run `pip -r requirements.txt`

# Usage
1. Clone the repository <b>OR</b> download the .ZIP file and extract it.
2. Install the needed modules.
3. Run the script using the `RUN_IN_BACKGROUND.bat`(if windows) or `pythonw battery.py`

The script will start running and will continuously monitor your battery percentage. When the battery reaches 100%, a notification will be displayed indicating that the battery is fully charged. When the battery reaches 80% and charging, another notification will be displayed reminding you to unplug your device. Finally, when the battery percentage drops below 30%, the script will display a notification reminding you to charge your device. (Default behavior)

#### Change this behaviour by editing the `config.json` using the `ConfigBuilder.html` website.

# Notes
Stop the script using `killswitch.py`