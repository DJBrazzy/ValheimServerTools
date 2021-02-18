start "" C:\Users\<username>\AppData\LocalLow\IronGate\Valheim\worlds\backup.py

@echo off
set SteamAppId=892970

echo "Starting server PRESS CTRL-C to exit"

REM Tip: Make a local copy of this script to avoid it being overwritten by steam.
REM NOTE: Minimum password length is 5 characters & Password cant be in the server name.
REM NOTE: You need to make sure the ports 2456-2458 is being forwarded to your server through your local router & firewall.
valheim_server -nographics -batchmode -name "The Raven" -port 2456 -world "Server1" -password "odinsbeard"

