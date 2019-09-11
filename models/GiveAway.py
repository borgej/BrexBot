__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class GiveAway():
    def __init__(self, id, trigger, prize, ends_at, mod, sub, follower, viewer):
        self.id = id
        self.trigger = trigger
        self.prize = prize
        self.ends_at = ends_at
        self.mod = mod
        self.sub = sub
        self.follower = follower
        self.viewer = viewer

        self.participants = []
        self.winners = []
