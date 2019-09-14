import unittest
from CommandHandler import CommandHandler
from models.Channel import Channel
from models.Command import Command
import Config

class CommandHandlerTest(unittest.TestCase):

    def test_command_exists_and_is_triggered(self):
        command = "!social"
        commandname = "social"
        message = Message(command, "randomuser")
        channel = Channel(Config.CHANNEL_NAME)
        channel.commands.append(
            Command(-1, Config.CHANNEL_NAME, "social", True, "Join my Discord at www.discord.com", True, True, True,
                    True, True, True, None, None))
        commandhandler = CommandHandler(channel)

        commandres, can_trigger = commandhandler.is_command_triggered(message)

        self.assertEqual(commandname, commandres.name)
        self.assertEqual(True, can_trigger)

    def test_command_exists_and_is_triggered_by_broadcaster(self):
        command = "!social"
        commandname = "social"
        message = Message(command, Config.CHANNEL_NAME)
        channel = Channel(Config.CHANNEL_NAME)
        channel.commands.append(
            Command(-1, Config.CHANNEL_NAME, "social", True, "Join my Discord at www.discord.com", True, False, False,
                    False, False, False, None, None))
        commandhandler = CommandHandler(channel)

        commandres, can_trigger = commandhandler.is_command_triggered(message)

        self.assertEqual(commandname, commandres.name)
        self.assertEqual(True, can_trigger)

    def test_command_exists_is_not_active_and_is_not_triggered(self):
        command = "!social"
        commandname = "social"
        message = Message(command, "randomuser")
        channel = Channel(Config.CHANNEL_NAME)
        channel.commands.append(
            Command(-1, Config.CHANNEL_NAME, "social", False, "Join my Discord at www.discord.com", True, True, True,
                    True, True, True, None, None))
        commandhandler = CommandHandler(channel)

        commandres, can_trigger = commandhandler.is_command_triggered(message)

        self.assertEqual(None, commandres)
        self.assertEqual(None, can_trigger)

    def test_command_exists_is_not_triggered(self):
        command = "!blizzard"
        commandname = "blizzard"
        message = Message(command, "randomuser")
        channel = Channel(Config.CHANNEL_NAME)
        channel.commands.append(
            Command(-1, Config.CHANNEL_NAME, "blizzard", True, "My Blizzard ID is UncleBob#199", True, False, False,
                    False, False, False, None, None))
        commandhandler = CommandHandler(channel)

        commandres, can_trigger = commandhandler.is_command_triggered(message)

        self.assertEqual(commandname, commandres.name)
        self.assertEqual(False, can_trigger)

    def test_command_does_not_exists_is_not_triggered(self):
        command = "!boguscommand"
        message = Message(command, "randomuser")
        channel = Channel(Config.CHANNEL_NAME)
        channel.commands.append(
            Command(-1, Config.CHANNEL_NAME, "Blizzard id", True, "My Blizzard ID is UncleBob#199", True, True, True,
                    False, False, False, None, None))
        commandhandler = CommandHandler(channel)

        commandres, can_trigger = commandhandler.is_command_triggered(message)

        self.assertEqual(None, commandres)
        self.assertEqual(None, can_trigger)

    def test_message_contains_command(self):
        command = "!uptime"
        commandname = "uptime"
        message = Message(command, "randomuser")
        channel = Channel(Config.CHANNEL_NAME)
        commandhandler = CommandHandler(channel)

        commandres, argumentres = commandhandler.message_contains_command(message)

        self.assertEqual(commandname, commandres)
        self.assertEqual(None, argumentres)

    def test_message_contains_command_with_arguments(self):
        command = "!bonus"
        commandname = "bonus"
        argument = "ToMiSmE 1000"
        message = Message(command + " " + argument, "randomuser")
        channel = Channel(Config.CHANNEL_NAME)
        commandhandler = CommandHandler(channel)

        commandres, argumentres = commandhandler.message_contains_command(message)

        self.assertEqual(commandname, commandres)
        self.assertEqual(argument, argumentres)

    def test_message_does_not_contain_command(self):
        message = Message("I just pooped my pants :(", "randomuser")
        channel = Channel(Config.CHANNEL_NAME)
        commandhandler = CommandHandler(channel)

        commandres, argumentres = commandhandler.message_contains_command(message)

        self.assertEqual(None, commandres)
        self.assertEqual(None, argumentres)

# Helper classes
class Message():
    def __init__(self, text, viewer_name):
        self.text = text
        self.user = User(viewer_name)
        self.channel = Config.CHANNEL_NAME

class User():
    def __init__(self, viewer_name):
        self.display_name = viewer_name
