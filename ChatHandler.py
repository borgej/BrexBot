import twitch
import logging


class ChatHandler(twitch):
    def __init__(self, channelname, nickname, oauth):
        self.nickname = nickname
        self.channel = "#" + channelname
        self.oauth = oauth
        self.chat_connection = None

        self.chat_log = []
        self.triggers = None
        self.polls = None
        self.banned_words = None

        self.logger = logging.getLogger()

    # Log chatmessage
    def logMessage(self, chatmessage):
        self.chat_log.append(chatmessage)

    # Update triggers if changed outside ChatHandler
    def set_triggers(self, triggers):
        self.triggers = triggers
        self.logger.info("Updated triggers")

    # Set banned words
    def set_banned_words(self, banned_words):
        self.banned_words = banned_words
        self.logger.info("Updated banned words")

    # Set polls
    def set_polls(self, polls):
        self.polls = polls
        self.logger.info("Updated polls")

    # Get the chat log
    def get_chat_log(self):
        return self.chat_log

    # Connect to chat
    def connectToChat(self, message_checker):
        try:
            self.chat_connection = self.Chat(channel=self.channel, nickname=self.nickname, oauth=self.oauth)
            self.chat_connection.subscribe(lambda message: message_checker(message))
            self.sendMessage("I just connected...")
            return self.chat_connection
        except Exception as e:
            self.logger.exception("Error on connecting to channel: " + self.channel)

    # Send message to chat
    def sendMessage(self, message):
        self.chat_connection.send(self.chat)
