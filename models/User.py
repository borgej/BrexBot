__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class User():
    def __init__(self, username, password, channel, bot_name, bot_oauth, channel_token, created, last_active):
        self.username = username
        self.password = password
        self.channel = channel
        self.bot_name = bot_name
        self.bot_oauth = bot_oauth
        self.channel_token = channel_token
        self.created = created
        self.last_active = last_active


