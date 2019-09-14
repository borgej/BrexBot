__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class Command():
    def __init__(self, id, channel, name, active, response, broadcaster, mod, sub, vip, follower, viewer, cooldown = None, lastrun = None):
        self.id = id
        self.channel = channel
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
        self.cool_down = cooldown
        self.lastrun = lastrun
