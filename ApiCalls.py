import json
import urllib
import requests
import Config
import logging

# Class to access the new Twitch 'HELIX' API
# The class receives it's authentication from a dictionary (HEADERS) in the Config.py file.
# The "Bearer" token must have the required scopes to perform successful API calls.


class ApiCalls:
    def __init__(self, channel_name=Config.CHANNEL_NAME):
        self.channel_id = self.get_user_id(channel_name)

    # Function to make a JSON request to the Twitch API
    def json_data(self, url, user=None):
        try:
            req = urllib.request.Request(url, headers=Config.HEADERS)
            resp = urllib.request.urlopen(req)
            twitch_data = json.loads(json.dumps(json.loads(resp.read())))
            return twitch_data
        except Exception as e:
            logging.error("Error parsing JSON data.")

    # Get the ID of a given username
    def get_user_id(self, username=Config.CHANNEL_NAME):
        try:
            url = 'https://api.twitch.tv/helix/users?login=' + username
            user_data = self.json_data(url, username)
            user_id = user_data['data'][0]['id']
            return user_id
        except Exception as e:
            logging.error("Unable to retrieve the user ID for " + username)

    # Gather all available data for a specified user
    def get_user_data(self, username=Config.CHANNEL_NAME):
        try:
            url = 'https://api.twitch.tv/helix/users?login=' + username
            user_data = self.json_data(url, username)
            user = user_data['data'][0]
            print(user)
            return user
        except Exception as e:
            logging.error("Unable to retrieve the data for " + username)

    def get_channel_id(self, channel_name=Config.CHANNEL_NAME):
        try:
            return self.channel_id
        except Exception as e:
            logging.error("Could not retrieve channel ID for " + channel_name)

    # Get first 100 moderators of a channel. "Pagination" must be used for more than 100 results.
    # Request requires a valid Bearer (Helix Oauth) token.
    def get_moderators(self):
        try:
            url = 'https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=' + self.channnel_id
            moderator_data = self.json_data(url)
            moderator_names = []
            for index, item in enumerate(moderator_data['data']):
                moderator_names.append(item['user_name'])
            return moderator_names
        except Exception as e:
            logging.error("Could not retrieve Moderator list for the channel")

    # Check if a specified user is a moderator in the channel
    def is_moderator(self, viewer):
        try:
            viewer_id = self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=' + self.channel_id + '&user_id=' + viewer_id
            moderator_data = self.json_data(url)
            if moderator_data is None:
                return False
            else:
                return True
        except Exception as e:
            logging.error("Unable to determin if " + viewer + " is a moderator.")

    # Check if a specified user is following the channel
    def is_follower(self, viewer):
        try:
            viewer_id =  self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/users/follows?to_id=' + self.channel_id + '&from_id=' + viewer_id
            follow_data = self.json_data(url)
            if follow_data['total'] == 0:
                return None
            else:
                return follow_data['data'][0]['followed_at']
        except Exception as e:
            logging.error("Unable to determin if " + viewer + " is following the channel.")

    # Check if a viewer is subscribed to teh channel
    def is_subscriber(self, viewer):
        try:
            viewer_id = self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/subscriptions?broadcaster_id=' + self.channel_id + '&user_id=' + viewer_id + '&tier'
            sub_data = self.json_data(url)
            return sub_data
        except Exception as e:
            logging.error("Unable to determin if " + viewer + " is subscribed to the channel.")

    # Creates a clip from the live stream. Test when live as
    # when not live it shows a previously created clip.
    def create_clip(self):
        try:
            url = 'https://api.twitch.tv/helix/clips?broadcaster_id=' + self.channel_id
            clip_data = self.json_data(url)
        except Exception as e:
            logging.error("Couldn't create clip.")

    # Check if a user is banned from the channel
    def is_banned(self, viewer):
        try:
            viewer_id = self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/moderation/banned?broadcaster_id=' + self.channel_id + '&user_id=' + viewer_id
            banned_data = self.json_data(url)
            if banned_data is None:
                return False
            else:
                return True
        except Exception as e:
            logging.error("Unable to check if " + viewer + " is banned from the channel.")

