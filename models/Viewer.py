__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

from TwitchApi import TwitchApi
from Db import Db
import Config


class Viewer(TwitchApi):

    def __init__(self, id, viewer, channel=Config.CHANNEL_NAME, points=None, last_gamble=None, last_roulette=None, is_subscriber=0):
        # This is the id of the channel the viewer is watching.
        self.id = id
        self.viewer = viewer
        self.user_id = self.get_user_id(viewer)
        self.channel = channel
        self.channel_id = self.get_user_id(Config.CHANNEL_NAME)
        self.points = points
        self.last_gamble = last_gamble
        self.last_roulette = last_roulette
        self.is_follower = self.is_follower(viewer)
        self.is_moderator = self.is_moderator(viewer)
        self.is_subscriber = is_subscriber #self.is_subscriber(viewer)
        self.is_broadcaster = self.viewer == self.channel

    def exists(self):
        media_check = Db().load_all('viewer')
        request_data = list(self.__dict__.values())

        for i in media_check:
            if i[0] == request_data[0] and i[2] == request_data[2]:
                return True
            else:
                continue
        return None

    def load(self):
        loyalty_data = Db().load_all('viewer', self.channel)
        current_status = self.__dict__
        for key, value in enumerate(current_status):
            current_status[value] = loyalty_data[key]
        return self

    def save(self):
        object_values = str(self.__dict__.values()).replace("None", "'None'")[13:-2]
        print(object_values)
        Db().save('viewer', object_values)
        return self

    def delete(self):
        request_id = str(self.__dict__.values())[13:14]
        Db().delete('viewer', request_id)