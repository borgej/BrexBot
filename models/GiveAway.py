__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class GiveAway():
    def __init__(self, id, channel, title, trigger, created, ending, mod, sub, follower, viewer, winner):
        self.id = id
        self.channel = channel
        self.title = title
        self.trigger = trigger
        self.created = created
        self.ending = ending
        self.mod = mod
        self.sub = sub
        self.follower = follower
        self.viewer = viewer
        self.winner = winner

        self.participants = []
        self.winners = []
