import subprocess
from classes import API

def executeSysCmd(cmd, arglist, noargs):
    # /execute dir [/d,/b]
    # pass list of args to arglist
    if noargs:
        try:
            out = subprocess.check_output(cmd)
            return out
        except subprocess.CalledProcessError as e:
            errorString = "Error encountered: {0}\n".format(e)
            return errorString
    else: 
        toExecute = []
        toExecute.append(cmd)
        for i in arglist:
            toExecute.append(i)
        try:
            out = subprocess.check_output(toExecute)
            return out
        except subprocess.CalledProcessError as e:
            errorString = "Error encountered: {0}\n".format(e)
            return errorString
