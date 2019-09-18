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
        self.is_subscriber = self.is_subscriber(viewer)
        self.is_broadcaster = self.viewer == self.channel

    def filter_values(self):
        values_list = self.__dict__
        for i in list(values_list):
            if i.startswith('_'):
                del values_list[i]
        return values_list

    def exists(self):
        db_data = Db().load_all('viewer')
        request_data = list(self.filter_values().values())
        for i in db_data:
            if i[0] == request_data[0] and i[2] == request_data[2]:
                return True
            else:
                continue
        return None

    def load(self):
        data = Db().load_by_id('viewer', self.id, self.channel)
        current_status = self.filter_values()
        for key, value in enumerate(current_status):
            current_status[value] = data[key]
        return self

    def save(self):
        filtered = str(self.filter_values().values()).replace("None", "'None'")[13:-2]
        Db().save('viewer', filtered)
        return self

    def delete(self):
        request_id = list(self.__dict__.values())
        Db().delete('viewer', request_id[0])

