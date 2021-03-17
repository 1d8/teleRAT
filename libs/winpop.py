import win32gui
def createMessage(text, caption):
    win32gui.MessageBox(0, text, caption, 0)