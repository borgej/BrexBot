import unittest
from TwitchApi import TwitchApi
import Config


class TestApiCalls(unittest.TestCase):

    def test_get_user_id(self):
        self.test = TwitchApi().get_user_id(Config.CHANNEL_NAME)
        self.assertNotEqual(int(self.test), None)
        return self.test

    def test_get_user_data(self):
        data_test = TwitchApi().get_user_data(Config.CHANNEL_NAME)
        self.assertNotEqual(data_test, None)

    def test_get_channel_id(self):
        channel_id = TwitchApi().get_channel_id(Config.CHANNEL_NAME)
        self.assertEqual(channel_id, self.test_get_user_id())

    def test_get_moderators(self):
        self.test_moderators = TwitchApi().get_moderators()
        self.assertEqual(self.test_moderators, ['ToMiSmE'])

    # The below also tests the "get_moderator" function.
    def test_is_moderator(self):
        moderators = TwitchApi().get_moderators()
        first_moderator = moderators[0]
        test_is_moderator = TwitchApi().is_moderator(first_moderator)
        self.assertEqual(test_is_moderator, True)

    def test_is_not_moderator(self):
        test_is_moderator = TwitchApi().is_moderator("BeeJeey")
        self.assertEqual(test_is_moderator, False)

    # The below also tests the "get_followers" function.
    def test_is_follower(self):
        followers = TwitchApi().get_followers()
        first_follower = followers[0]
        test_is_follower = TwitchApi().is_follower(first_follower)
        self.assertNotEqual(None, test_is_follower)

if __name__ == '__main__':
    unittest.main()
