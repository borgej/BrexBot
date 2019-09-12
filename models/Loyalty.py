__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class Loyalty():
    def __init__(self, id, channel, loot_name, interval, amount, sub_bonus):
        self.id = id
        self.channel = channel
        self.loot_name = loot_name
        self.interval = interval
        self.amount = amount
        # sub's get amount + sub bonus at each interval
        self.sub_bonus = sub_bonus
