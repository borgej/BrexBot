__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

from TwitchApi import TwitchApi


class Viewer(TwitchApi):

    def __init__(self, viewer):
        self.viewer = viewer
        self.user_id = self.get_user_id(viewer)
        self.follower = self.is_follower(self.user_id)
        self.moderator = self.is_moderator(self.user_id)
        self.subscriber = self.is_subscriber(self.user_id)
