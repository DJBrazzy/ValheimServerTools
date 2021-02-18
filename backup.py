import sys
import getopt
import shutil
import os
import time
from datetime import datetime

def main(argv):
    pathname = os.path.dirname(sys.argv[0])
    folderPath = os.path.abspath(pathname)
    backupPath = os.path.abspath(pathname) +'\\backup'
    timer = 900
    numBackups = 2
    backupCount = 0

    print('fpath' + folderPath)
    print('bpath' + backupPath)

    ## parse arguments
    try:
        opts, args = getopt.getopt(argv, "hf:b:t:n:", ["ffile=","bfile=","timer=","numbackups="])
    except getopt.GetoptError:
        print('backup.py requires parameters: -f <folder path> -b <backup path>')
        print('error fetching parameters')
        sys.exit(2)
    if len(opts) < 0:
        print('backup.py requires parameters: -f <folder path> -b <backup path>')
        print('no parameters found')
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print('\n================================================================================\n')
            print('backup.py -f <folder path> -b <backup path> -t <delay between backups> -n <number of backup folders to maintain>\n')
            print('\t-f is expected to be a directory/folder, not a file')
            print('\t-b is also expected to be a directory. If no such directory exists at this path, it will be created')
            print('\t-t changes the amount of time between backups in seconds')
            print('\t-n is the number of backups to make.')
            print('\t\tFor example: "-n 2": every -t seconds backups will alternate between <backup path>0 and <backup path>1')
            print('\t\tThis is useful for backing up files that may be edited during the backup process.\n')
            sys.exit()
        elif opt in ("-f", "--ffile"):
            folderPath = arg
        elif opt in ("-b", "--bfile"):
            backupPath = arg
        elif opt in ("-t", "--timer"):
            timer = int(arg)
        elif opt in ("-n", "--numbackups"):
            numBackups = int(arg)
    print('Duplicating ' + folderPath + ' contents to ' + backupPath)
    print('Running backup every ' + str(timer) + ' seconds. Maintaining ' + str(numBackups)+' backups')

    ## Start backup cycle
    while True:
        now = datetime.now()
        backupCount += 1
        print(now.strftime("%H:%M:%S") + 'Running backup ' + str(backupCount) +'...')
        currentBackupPath = backupPath

        if numBackups > 1:
            currentBackupPath = backupPath + str(backupCount % numBackups)
            print(currentBackupPath)

        if os.path.exists(currentBackupPath) == False:
            print("Backup path doesn't exist, creating backup folder at " + currentBackupPath)
            os.makedirs(currentBackupPath)

        with os.scandir(folderPath) as folder:
            for file in folder:
                filePath = os.path.join(folderPath,file)
                if os.path.isfile(filePath):
                    print(file.name)
                    shutil.copy(filePath,currentBackupPath)
        
        time.sleep(timer)


    sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])