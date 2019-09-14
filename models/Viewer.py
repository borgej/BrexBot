__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

from TwitchApi import TwitchApi
import Config


class Viewer(TwitchApi):

    def __init__(self, viewer, channel = Config.CHANNEL_NAME, points = None, last_gamble = None, last_roulette = None):
        # This is the id of the channel the viewer is watching.
        self.id = id
        self.channel = channel
        self.channel_id = self.get_user_id(Config.CHANNEL_NAME)
        self.viewer = viewer
        self.points = points
        self.last_gamble = last_gamble
        self.last_roulette = last_roulette
        self.user_id = self.get_user_id(viewer)
        self.is_follower = self.is_follower(viewer)
        self.is_moderator = self.is_moderator(viewer)
        self.is_subscriber = self.is_subscriber(viewer)
        self.is_broadcaster = self.viewer == self.channel

