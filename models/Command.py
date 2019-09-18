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

    def filter_values(self):
        values_list = self.__dict__
        for i in list(values_list):
            if i.startswith('_'):
                del values_list[i]
        return values_list

    def exists(self):
        db_data = Db().load_all('command')
        request_data = list(self.filter_values().values())
        for i in db_data:
            if i[0] == request_data[0] and i[2] == request_data[2]:
                return True
            else:
                continue
        return None

    def load(self):
        data = Db().load_by_id('command', self.id, self.channel)
        current_status = self.filter_values()
        for key, value in enumerate(current_status):
            current_status[value] = data[key]
        return self

    def save(self):
        filtered = str(self.filter_values().values()).replace("None", "'None'")[13:-2]
        Db().save('command', filtered)
        return self

    def delete(self):
        request_id = list(self.__dict__.values())
        Db().delete('command', request_id[0])

