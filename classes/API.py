import requests, json
from classes import message
# interacting with Telegram api

class API:
    # when creating object based on this class, pass the API key as a param
    def __init__(self, apiSecret):
        self.apiSecret = apiSecret
        if len(self.apiSecret) < 46:
            print("Invalid API Key!")
            return
    
    def GetMessage(self):
        # grab recent message/cmd
        url = "https://api.telegram.org/bot{0}/getUpdates".format(self.apiSecret)
        response = requests.get(url)
        responseMap = response.json()
        try:
            recentMessageIndex = len(responseMap["result"])-1
            messageObj = message.MessageData(responseMap["result"][recentMessageIndex]["message"]["message_id"], responseMap["result"][recentMessageIndex]["message"]["chat"]["id"], responseMap["result"][recentMessageIndex]["message"]["text"])
            return messageObj
        except IndexError:
            # There are no messages for the day.
            return


    def SendResult(self, chatID, messageID, messageText):
        # upload result of executed cmd
        url = "https://api.telegram.org/bot{0}/sendMessage".format(self.apiSecret)
        jsonDat = {
            "chat_id": str(chatID),
            "text": str(messageText),
            "reply_to_message_id": int(messageID),
        }
        response = requests.post(url, json=jsonDat)
        #print(response.text)
        return


    def ErrorLogger(self, chatID, errorText):
        # use SendResult for sending error data
        url = "https://api.telegram.org/bot{0}/sendMessage".format(self.apiSecret)
        fullErrorText = "Error message: \n" + str(errorText)
        jsonDat = {
            "chat_id": str(chatID),
            "text": fullErrorText,
        }
        response = requests.post(url, json=jsonDat)
        return

    def UploadLocalFile(self, chatID, filepath):
        url = "https://api.telegram.org/bot{0}/sendDocument?chat_id={1}".format(self.apiSecret, str(chatID))
        fileHandle = open(filepath, 'rb')
        response = requests.post(url, files={"document": fileHandle})
        #print(response.text)
        return

    def UploadPhoto(self, chatID, photopath):
        url = "https://api.telegram.org/bot{0}/sendPhoto?chat_id={1}".format(self.apiSecret, str(chatID))
        fileHandle = open(photopath, 'rb')
        response = requests.post(url, files={"photo": fileHandle})
        #print(response.text)
        return