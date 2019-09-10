import unittest
from ChatHandler import ChatHandler
import twitch
import logging

class ChatHandlerTest(unittest.TestCase):
    def test_connect_to_chat(self):
        # Change values to actual values, test should pass with message in chat saying "I just connected..."
        self.channel = "channelname"
        self.nickname = "botusername"
        self.oauth = "oauth:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

        test = ChatHandler(self.channel, self.nickname, self.oauth)
        test.connect_to_chat(self.void_function, verbose_connect = True)

        self.assertEqual(test.chat_connection.joined, True)
        self.assertEqual(test.chat_connection.channel, self.channel)

    # helper function
    def void_function(self, message):
        pass;
