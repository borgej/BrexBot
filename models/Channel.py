__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class Channel():
    def __init__(self, channel, game, title, mature):
        self.channel = channel
        self.broadcaster_language = None
        self.followers = None
        self.game = game
        self.mature = mature
        # Title of the stream
        self.status = title

        self.followers = []
        self.subscribers = []
        self.moderators = []
        self.views = None

        self.banned_users = []

        self.clips = []
        self.vods = []

