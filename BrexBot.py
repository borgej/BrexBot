__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import logging
from Db import Db


logging.basicConfig(level=logging.DEBUG)
logging.debug('This will get logged')

con = Db()
# con.viewer_exists("tomisme", "tomisme")
# con.create_viewer("tomisme", "tomisme", 546)
#viewer_list = "tomisme"
#con.remove_points("tomisme", "tomisme", 12000)
# con.add_last_game_time("tomisme", "tomisme", "dice")
con.time_since_last_gamble("tomisme", "tomisme")