from twitch import TwitchClient

class TwitchTest:
    def __init__(self):
        #Create a client using the "TwitchClient" connection
        # self.client = TwitchClient(client_id='i6a33w342uxukr28axfjppf0zvsrbz', oauth_token='oauth:qdg13wxdcuuovuyl08sf1ar84h7sjx')
        self.client = TwitchClient('gokkk5ean0yksozv0ctvljwqpceuin', 'oauth:gox8ache7pazv7lufoaio4es6v3d4u')

    def get_id(self, username):
        user_info = self.client.users.translate_usernames_to_ids(username)
        return user_info[0].get("id")

    def get_channel_info(self, username):
        channel_id = self.get_id(username)
        channel_info = self.client.channels.get_by_id(channel_id)
        print(channel_info)

    # This wont work until the application is authenticated on the channel
    def check_if_subscribed(self, viewer, channel):
        viewer_id = self.get_id(viewer)
        channel_id =  self.get_id(channel)
        is_subscribed = self.client.users.check_subscribed_to_channel(viewer_id, channel_id)
        print(is_subscribed)
        #return self.client.users.check_subscribed_to_channel(viewer_id, channel_id)

