import json
import urllib
import requests
import Config
import logging

logging.basicConfig(level=logging.DEBUG)


# Class to access the new Twitch 'HELIX' API
# The class receives it's authentication from a dictionary (HEADERS) in the Config.py file.
# The "Bearer" token must have the required scopes to perform successful API calls.
class TwitchApi:
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
            logging.error("Error parsing JSON data.", e)

    # Get the ID of a given username
    def get_user_id(self, username=Config.CHANNEL_NAME):
        try:
            url = 'https://api.twitch.tv/helix/users?login=' + username
            user_data = self.json_data(url, username)
            user_id = user_data['data'][0]['id']
            return user_id
        except Exception as e:
            logging.error("Unable to retrieve the user ID for " + username, e)

    # Gather all available data for a specified user
    def get_user_data(self, username=Config.CHANNEL_NAME):
        try:
            url = 'https://api.twitch.tv/helix/users?login=' + username
            user_data = self.json_data(url, username)
            user = user_data['data'][0]
            return user
        except Exception as e:
            logging.error("Unable to retrieve the data for " + username, e)

    def get_channel_id(self, channel_name=Config.CHANNEL_NAME):
        try:
            return self.channel_id
        except Exception as e:
            logging.error("Could not retrieve channel ID for " + channel_name, e)

    # Get first 100 moderators of a channel. "Pagination" must be used for more than 100 results.
    # Request requires a valid Bearer (Helix Oauth) token.
    def get_moderators(self):
        try:
            url = 'https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=' + self.channel_id
            moderator_data = self.json_data(url)
            moderator_names = []
            for index, item in enumerate(moderator_data['data']):
                moderator_names.append(item['user_name'])
            return moderator_names
        except Exception as e:
            logging.error("Could not retrieve Moderator list for the channel", e)

    def get_followers(self):
        try:
            url = 'https://api.twitch.tv/helix/users/follows?to_id=' + self.channel_id
            follower_data = self.json_data(url)
            follower_names = []
            for index, item in enumerate(follower_data['data']):
                follower_names.append(item['from_name'])
            return follower_names
        except Exception as e:
            logging.error("Could not retrieve Follower list for the channel", e)

    # Check if a specified user is a moderator in the channel
    def is_moderator(self, viewer):
        try:
            viewer_id = self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/moderation/moderators?broadcaster_id=' + self.channel_id + '&user_id=' + viewer_id
            moderator_data = self.json_data(url)
            if moderator_data['data'] is None:
                return False
            else:
                return True
        except Exception as e:
            logging.error("Unable to determine if " + viewer + " is a moderator.", e)

    # Check if a specified user is following the channel
    def is_follower(self, viewer):
        try:
            viewer_id = self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/users/follows?to_id=' + self.channel_id + '&from_id=' + viewer_id
            follow_data = self.json_data(url)
            if follow_data['total'] == 0:
                return False
            else:
                return True
        except Exception as e:
            logging.error("Unable to determine if " + viewer + " is following the channel.", e)

    # Check if a viewer is subscribed to teh channel
    def is_subscriber(self, viewer):
        try:
            viewer_id = self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/subscriptions?broadcaster_id=' + self.channel_id + '&user_id=' + viewer_id + '&tier'
            sub_data = self.json_data(url)
            if not sub_data['data']:
                return False
            else:
                return True
        except Exception as e:
            logging.error("Unable to determin if " + viewer + " is subscribed to the channel.", e)

    # Creates a clip from the live stream. Test when live as
    # when not live it shows a previously created clip.
    def create_clip(self):
        try:
            url = 'https://api.twitch.tv/helix/clips?broadcaster_id=' + self.channel_id
            clip_data = self.json_data(url)
            return clip_data
        except Exception as e:
            logging.error("Couldn't create clip.", e)

    # Check if a user is banned from the channel
    def is_banned(self, viewer):
        try:
            viewer_id = self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/moderation/banned?broadcaster_id=' + self.channel_id + '&user_id=' + viewer_id
            banned_data = self.json_data(url)
            if banned_data['data'] is None:
                return False
            else:
                return True
        except Exception as e:
            logging.error("Unable to check if " + viewer + " is banned from the channel.", e)

    # Get followed channel since date
    def follower_since(self, viewer):
        try:
            viewer_id = self.get_user_id(viewer)
            url = 'https://api.twitch.tv/helix/users/follows?to_id=' + self.channel_id + '&from_id=' + viewer_id
            follow_data = self.json_data(url)
            if follow_data['total'] == 0:
                return None
            else:
                return follow_data['data'][0]['followed_at']
        except Exception as e:
            logging.error("Unable to determine if " + viewer + " is following the channel.", e)

    # The following functions use the Twitch V5 API and require a separate token (OAuth)
    def update_channel(self, title, game):
        try:
            url = 'https://api.twitch.tv/kraken/channels/' + self.get_channel_id() + '?api_version=5'
            headers = Config.V5HEADERS
            data = {'channel[status]': title, 'channel[game]': game, 'channel[channel_feed_enabled]': 'true'}
            response = requests.put(url=url, headers=headers, params=data)
            return response
        except Exception as e:
            logging.error('Unable to perform V5 API call', e)
            return None

    # The below will retrieve current "Chatters" in a channel.
    # THESE ARE NOT A TWITCH API FUNCTIONS - UNDOCUMENTED
    # This has a delayed refresh time (currently unknown).
    # Note: Due to some viewers/bots being connected anon to the channel
    # this will only show chatters and not all viewers.
    def get_chatter_data(self, channel):
        try:
            url = 'https://tmi.twitch.tv/group/user/' + channel + '/chatters'
            chatter_data = self.json_data(url)
            return chatter_data
        except Exception as e:
            logging.error('Unable to retrieve chatter data. ', e)
            return None

    def all_chatter_names(self, channel):
        try:
            chatter_data = self.get_chatter_data(channel)['chatters']
            chatters = [item for sublist in chatter_data.values() for item in sublist]
            return chatters
        except Exception as e:
            logging.error('Unable to retrieve chatter names. ', e)
            return None
