__author__ = "Børge Jakobsen, Thomas Donegan"
__copyright__ = "Copyright 2019, Brexit boy and SaLmon king"
__credits__ = ["Børge Jakobsen, Thomas Donegan"]
__license__ = "Apache License"
__version__ = "2.0"
__maintainer__ = "Børge Jakobsen, Thomas Donegan"
__status__ = "Development"

import logging
import json
import pprint
import urllib
import urllib.request
import urllib.parse
import Config
from models.MediaRequest import MediaRequest


logging.basicConfig(level=logging.DEBUG)

# Media request handler to search for video/songrequests on YouTube
class MediaRequestHandler():
    def __init__(self):
        self.api_key = Config.YOUTUBE_KEY

    def search_request(self, request: MediaRequest):
        try:
            if(request.title == None):
                logging.debug("No title in request, not searching")
                return None
            logging.debug("Searching for: '" + request.title +"'")

            search_url_snippet = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=relevance&q=" + urllib.parse.quote(request.title) + "&key=" + self.api_key
            response_snippet = urllib.request.urlopen(search_url_snippet).read()
            dataSnippet = json.loads(response_snippet)

            logging.debug("Found " + str(len(dataSnippet['items'])) + " matches for '" + request.title +"'")

            all_data_snippet = dataSnippet['items']
            request.video_id = all_data_snippet[0]['id']['videoId']
            request.title = all_data_snippet[0]['snippet']['title']
            request.url = "https://www.youtube.com/watch?v=" +request.video_id

            logging.debug("Selected " + request.title + " with url " + request.url)

            return request

        except Exception as e:
            logging.exception("Exception in search call to YouTube ", e)
            return None

    def get_video_details(self, request: MediaRequest):
        try:
            search_url_snippet = "https://www.googleapis.com/youtube/v3/videos?id=" + request.video_id + "&key=" + self.api_key + "&part=snippet"
            search_url_content_details = "https://www.googleapis.com/youtube/v3/videos?id=" + request.video_id + "&key=" + self.api_key + "&part=contentDetails"

            response_snippet = urllib.request.urlopen(search_url_snippet).read()
            response_content_details = urllib.request.urlopen(search_url_content_details).read()

            dataSnippet = json.loads(response_snippet)
            dataContentDetails = json.loads(response_content_details)

            all_data_snippet = dataSnippet['items']
            all_data_content_details = dataContentDetails['items']
            contentDetails = all_data_snippet[0]['snippet']
            length = all_data_content_details[0]['contentDetails']

            request.title = contentDetails['title']
            request.thumbnail_url = contentDetails['thumbnails']['default']['url']
            request.length = length['duration']

            logging.debug("Video id: " + request.video_id + " gave this data: title: " + request.title + " length: " + request.length )

            return request

        except Exception as e:
            logging.exception("Exception in get_video call to YouTube ", e)
            return None
