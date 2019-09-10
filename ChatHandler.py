import twitch
import logging


class ChatHandler():
    def __init__(self, channelname, nickname, oauth, commands = None, triggers = None, polls = None, banned_words = None):
        self.nickname = nickname
        self.channel = "#" + channelname
        self.oauth = oauth
        self.chat_connection = None

        self.chat_log = []
        self.commands = commands
        self.triggers = triggers
        self.polls = polls
        self.banned_words = banned_words

        self.logger = logging.getLogger()

    # Log chatmessage
    def log_message(self, chat_message):
        self.chat_log.append(chat_message)

    # Update commands if changed outside ChatHandler
    def set_commands(self, commands):
        self.commands = commands
        self.logger.info("Updated commands")

    # Update triggers if changed outside ChatHandler
    def set_triggers(self, triggers):
        self.triggers = triggers
        self.logger.info("Updated triggers")

    # Update banned words if changed outside ChatHandler
    def set_banned_words(self, banned_words):
        self.banned_words = banned_words
        self.logger.info("Updated banned words")

    # Update polls if changed outside ChatHandler
    def set_polls(self, polls):
        self.polls = polls
        self.logger.info("Updated polls")

    # Get the chat log
    def get_chat_log(self):
        return self.chat_log

    # Connect to chat
    def connect_to_chat(self, message_checker, verbose_connect = False):
        try:
            self.chat_connection = twitch.Chat(channel=self.channel, nickname=self.nickname, oauth=self.oauth)

            # call message_checker on every received message
            self.chat_connection.subscribe(lambda message: message_checker(message))
            # Log every message
            self.chat_connection.subscribe(lambda message: self.log_message(message))

            # Advertise connect in channel if set
            if(verbose_connect):
                self.send_message("I just connected...")

            self.logger.info("Connected to channel: " + self.channel)

            return self.chat_connection

        except Exception as e:
            self.logger.exception("Error connecting to channel: " + self.channel)

    # Send message to chat
    def send_message(self, message):
        try:
            self.chat_connection.send(message)
        except Exception as e:
            self.logger.exception("Error sending chat message: " + message)
