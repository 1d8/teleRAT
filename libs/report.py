from libs import shell
def hardwareInfo():
    hardwareInfo = shell.executeSysCmd("cmd.exe /c systeminfo", "", True)
    return hardwareInfo

def softwareInfo():
    osVersion = shell.executeSysCmd("cmd.exe /c ver", "", True)
    return osVersion