__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import logging
import re
import Config
from models.Channel import Channel
from models.Viewer import Viewer

logging.basicConfig(level=logging.DEBUG)

# Media request handler to search for video/songrequests on YouTube
class CommandHandler():
    def __init__(self, channel: Channel):
        self.prefix = Config.COMMAND_PREFIX
        self.commands = channel.commands

    def is_command_triggered(self, message):
        command_typed, arguments = self.message_contains_command(message)
        if(command_typed != None):
            # check all commands in channel
            for c in self.commands:
                # check if command is in commands and is active
                if(c.name == str(command_typed).lower() and c.active == True):
                    # command found, check if viewer can trigger
                    if(self.can_trigger_command(message, c)):
                        return c, True
                    # viewer can't trigger command
                    else:
                        return c, False
            # command not in list
            return None, None
        else:
            return None, None

    # Function to check if a user who sent a message can tigger given command
    # TODO: TwitchAPI.is_subscriber needs to be uniform to support being called for True/False
    def can_trigger_command(self, message, command):
        viewer = Viewer(message.user.display_name)

        if (command.broadcaster == True and viewer.is_broadcaster == True):
            return True
        elif (command.mod == True and viewer.is_moderator == True):
            return True
        elif (command.sub == True and viewer.is_subscriber == True):
            return True
        elif(command.follower == True and viewer.is_follower == True):
            return True
        elif (command.viewer):
            return True
        else:
            return False

    # Function to check if a chat message contains a command
    # returns Command, Arguments
    def message_contains_command(self, message):
        try:
            # check for any commands and parameters to command
            match = re.match(r'' + self.prefix + '(\w*|\d*)\s*(.*)', message.text)

            # no match at all
            if(match == None):
                return None, None
            # check for command
            elif (len(match.groups()) > 0):
                # command with command arguments
                # return command as first parameter and command arguments as second parameters
                if (len(match.groups()) > 1):
                    command = match.group(1)
                    arguments = match.group(2)

                    if(str(arguments) == ""):
                        arguments = None
                        logging.debug("Command: '" + self.prefix + match.group(1) + "' typed by: " + message.user.display_name)
                    else:
                        logging.debug("Command: '" + self.prefix + match.group(1) + "' with arguments: '" + match.group(2) + "' typed by: " + message.user.display_name)
                    return command, arguments

                # command without arguments
                # return command as first parameter and None as arguments
                else:
                    command = match.group(1)
                    return command, None
            else:
                return None, None
        except Exception as e:
            logging.exception("Error checking message for command", e)
            return None, None
