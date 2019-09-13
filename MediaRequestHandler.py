__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import logging
import urllib.request
import urllib.parse
import re
import requests
import pprint
from lxml import html
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
            html_content = html_content.read().decode()
            search_results_video_id = re.findall(r'href=\"\/watch\?v=(.{11})', html_content)

            if(len(search_results_video_id) > 0):
                hits = len(search_results_video_id)
                logging.debug("Found " + str(hits) + " hits for '" + request.title +"'")
                request.video_id = search_results_video_id[0]
                request.url = "http://www.youtube.com/watch?v=" + request.video_id
                logging.debug("Search for '" + request.title + "' gave video_id: " + request.video_id + " and url: " + request.url)
                return request
        except ConnectionError:
            logging.exception("Exception in search call to YouTube ")
            return None

    def get_video_details(self, request: MediaRequest):
        try:
            pp = pprint.PrettyPrinter(indent=4)
            html_content = urllib.request.urlopen(request.url)
            tree = html.fromstring(html_content.read())

            request.title = tree.xpath('*//ytd-video-primary-info-renderer/div/h1/yt-formatted-string')
            request.length = tree.xpath('*//ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[29]/div[2]/div[1]/div/span[3]')
            
            pp.pprint(request.title)
            pp.pprint(request.length)

            logging.debug("Video details gave '" + request.title + "' with a length of: " + request.length)
            return request
        except:
            logging.exception("Exception in get_video call to YouTube")
            return None

