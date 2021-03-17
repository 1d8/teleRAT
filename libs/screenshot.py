import pyautogui, os.path, random, time

def takeScreenshot(numOfScreenshots):
    paths = []
    for i in range(int(numOfScreenshots)):
        randomInt = random.randint(1, 5)
        randomInt = str(randomInt)
        #tmpPath = os.path.expandvars("/home/nikola/Downloads")
        tmpPath = "/home/nikola/Downloads/" + str(randomInt) + ".png"
        #tmpPath += "\\" + randomInt
        time.sleep(int(randomInt))
        screenSnap = pyautogui.screenshot()
        screenSnap.save(tmpPath)
        paths.append(tmpPath)
    return paths
