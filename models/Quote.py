__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

class Quote():
    def __init__(self, id, nr, quote, user, quote_date):
        self.id = id
        self.nr = nr
        self.quote = quote
        self.user = user
        self.quote_date = quote_date
