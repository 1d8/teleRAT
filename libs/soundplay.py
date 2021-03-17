import winsound
# duration in milliseconds
def playSound(soundType):
        # play sound in loop
    if soundType == "asterisk":
        try:
             winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS|winsound.SND_LOOP|winsound.SND_ASYNC)
        except:
            return "Error encountered while attempting to play sound!"
    elif soundType == "exclamation":
        try:
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS|winsound.SND_LOOP|winsound.SND_ASYNC)
        except:
            return "Error encountered while attempting to play sound!"
    elif soundType == "exit":
        try:
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS|winsound.SND_LOOP|winsound.SND_ASYNC)
        except:
            return "Error encountered while attempting to play sound!"
    elif soundType == "hand":
        try:
            winsound.PlaySound("SystemHand", winsound.SND_ALIAS|winsound.SND_LOOP|winsound.SND_ASYNC)
        except:
            return "Error encountered while attempting to play sound!"
    elif soundType == "question":
        try:
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS|winsound.SND_LOOP|winsound.SND_ASYNC)
        except:
            return "Error encountered while attempting to play sound!"
    elif soundType == "beep":
        winsound.Beep(32600, 60000)
    else:
        return "Sound type specified doesn't exist. Please look at help menu!"