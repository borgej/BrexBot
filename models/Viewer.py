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

    def __init__(self, viewer):
        # This is the id of the channel the viewer is watching.
        self.channel_id = self.get_user_id(Config.CHANNEL_NAME)

        self.user_id = self.get_user_id(viewer)
        self.is_follower = self.is_follower(viewer)
        self.is_moderator = self.is_moderator(viewer)
        self.is_subscriber = self.is_subscriber(viewer)
