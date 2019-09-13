__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

from TwitchApi import TwitchApi


class Channel():
    def __init__(self, channel):
        self.channel = channel
        self.broadcaster_language = None
        self.game = None
        self.mature = None
        # Title of the stream
        self.status = None

        # Values retrieved from API
        self.followers = None
        self.subscribers = None
        self.moderators = []
        self.views = None

        # Database channel data
        self.media_requests = []
        self.polls = []
        self.quotes = []
        self.commands = []
        self.timers = []
        self.banned_words = []

        self.dbconn = Db()
        self.api = TwitchApi(self.channel)

    # load channel data from TwitchAPI and Database
    def load(self):
        self.followers = self.api.get_followers().count()
        self.moderators = self.api.get_moderators()


