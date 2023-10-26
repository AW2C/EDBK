import os
import zipfile
import time

global confFile 
confFile = "C:/Users/"+os.getenv("username")+"/AppData/Local/AW2C/EDBK/config.txt"

global EDdir
EDdir = "C:/Users/"+os.getenv("Username")+"/AppData/Local/Frontier Developments/Elite Dangerous"

def writeBackupDir(dir, button):
    with open(confFile, "r") as f:
        confArr = f.readlines()
        confArr[0] = dir
    with open(confFile, "w") as f:
        f.writelines(confArr)
    
    return

def updateLastBackup(time):
    with open(confFile, "r") as f:
        confArr = f.readlines()
        confArr[1] = time
        return

def conf(i):
    with open(confFile, "r") as f:
        confArr = f.readlines()
        return confArr[i]
    
def zipdir(path):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            zipfile.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(path, '..')))


def backup():
    dest = conf(0)
    with zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(EDdir, zipf)
    updateLastBackup(time.strftime("%d/%m/%Y %H:%M:%S"))
    


