__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

from Db import Db


class Command:
    def __init__(self, id, channel, command, name, active, response, broadcaster, mod, sub, vip, follower, viewer, cool_down=None, last_run=None, timer_interval=1):
        self.id = id
        self.channel = channel
        self.command = command
        self.name = name
        self.active = active
        self.response = response

        # Eligible users to trigger command
        self.broadcaster = broadcaster
        self.mod = mod
        self.sub = sub
        self.vip = vip
        self.follower = follower
        self.viewer = viewer

        # Set universal command cool down
        self.cool_down = cool_down
        self.last_run = last_run
        self.timer_interval = timer_interval

    def exists(self):
        media_check = Db().load_all('command')
        request_data = list(self.__dict__.values())

        for i in media_check:
            if i[0] == request_data[0] and i[2] == request_data[2]:
                return True
            else:
                continue
        return None

    def load(self):
        loyalty_data = Db().load_all('command', self.channel)
        current_status = self.__dict__
        for key, value in enumerate(current_status):
            current_status[value] = loyalty_data[key]
        return self

    def save(self):
        object_values = str(self.__dict__.values()).replace("None", "'None'")[13:-2]
        print(object_values)
        Db().save('command', object_values)
        return self

    def delete(self):
        request_id = str(self.__dict__.values())[13:14]
        Db().delete('command', request_id)