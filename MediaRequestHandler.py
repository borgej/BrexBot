__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import logging
import os
import urllib.request
import urllib.parse
import re
import Config
from models.MediaRequest import MediaRequest

logging.basicConfig(level=logging.DEBUG)

# Media request handler to search for video/songrequests on YouTube
# TODO: - Add tests
#       - Get title from chosen result
#       - Get number of views from chosen result
class MediaRequestHandler():
    def __init__(self):
        pass

    def search_request(self, request: MediaRequest):
        try:
            if(request.title == None):
                logging.debug("No title in request, not searching")
                return None

            logging.debug("Searching for: '" + request.title +"'")

            query_string = urllib.parse.urlencode({"search_query": request.title})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results_video_id = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

            if(len(search_results_video_id) > 0):
                logging.debug("Found " + str(len(search_results_video_id)) + " hits for '" + request.title +"'")
                request.id = search_results_video_id[0]
                request.url = "http://www.youtube.com/watch?v=" + request.id
                return request
        except ConnectionError:
            logging.exception("Exception in search YouTube API")
        finally:
            return None
