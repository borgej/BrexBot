__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import models.Command

class Timer(models.Command):
    def __init__(self, id, channel, command, active, response, broadcaster, mod, sub, vip, follower, viewer, cooldown = None, timer_interval = None, timer_last_run = None):
        # Interval in minutes
        self.timer_interval = timer_interval
        # Last time timer ran
        self.timer_last_run = timer_last_run
        super(Timer, self).__init__(id, channel, command, active, response, broadcaster, mod, sub, vip, follower, viewer, cooldown)

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

