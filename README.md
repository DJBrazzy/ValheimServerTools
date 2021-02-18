# Valheim Server Tools

At the moment just a backup script and updated .bat file to launch the backup script when starting the server.

## Backup Script
**This script was written with and has only been tested on python 3.8.6**
backup.py is a small python script to backup your worlds. To use the script do the following:
1. download backup.py
2. place backup.py in your worlds folder - by default this is C:\Users\<username>\AppData\LocalLow\IronGate\Valheim\worlds
3. Execute using "python backup.py"
4. By default backups will be created in the script folder
	- Change which folder is backed up using -f <folder to backup>
	- Change where backups are saved using -b <backup folder>
	- Change frequency of backups using -t <number of seconds between backups> (defaults to 900 seconds/15 minutes)
	- Change the number of versions to maintain using -n <number of versions> (defaults to 2)
	
## Updated .bat
The updated .bat file automatically starts the backup script before you start the server.
To use the updated .bat file:
1. Download start_headless_server.bat
2. Update the path in the first line with the path of your backup script
3. If you want to change the script arguments, append them to the first line
	- ex. change ```start "" C:\Users\david\AppData\LocalLow\IronGate\Valheim\worlds\backup.py``` to ```start "" C:\Users\david\AppData\LocalLow\IronGate\Valheim\worlds\backup.py -t 600```
4. Ensure your server isn't currently running, then run your updated start_headless_server.bat
5. You should see the standard server terminal open as well as the python terminal open with output regarding backup.py


