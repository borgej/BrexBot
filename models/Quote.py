__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class Quote():
    def __init__(self, id, channel, nr, quote, viewer, created):
        self.id = id
        self.channel = channel
        self.nr = nr
        self.quote = quote
        self.viewer = viewer
        self.created = created
