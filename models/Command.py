__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class Command():
    def __init__(self, id, channel, command, active, response, broadcaster, mod, sub, vip, follower, viewer, cooldown = None):
        self.id = id
        self.channel = channel
        self.command = command
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

    # Check if user can call command
    def can_trigger(self, stream_viewer):
        if (stream_viewer.is_broadcaster and self.broadcaster):
            return True
        if(stream_viewer.is_viewer and self.viewer):
            return True
        elif(stream_viewer.is_follower and self.follower):
            return True
        elif (stream_viewer.is_vip and self.vip):
            return True
        elif (stream_viewer.is_subscriber and self.sub):
            return True
        elif (stream_viewer.is_mod and self.mod):
            return True

        return False
