class MessageData:
    def __init__(self, messageID, chatID, messageText):
        self.messageID = messageID
        self.chatID = chatID
        self.messageText = messageText
    def ChatID(self):
        return self.chatID
    def MessageID(self):
        return self.messageID
    def MessageText(self):
        return self.messageText