import win32clipboard
def returnData():
    win32clipboard.OpenClipboard()
    return win32clipboard.GetClipboardData()