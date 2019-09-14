import unittest
import mysql.connector
from Db import Db
from models.User import User
from datetime import datetime


class Test(unittest.TestCase):
    def test_create_user(self):
        username = "normaltwitchuser@twitch.tv"
        dbconn = Db()

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        user = User(username, "userpassword", "testchannel", "testbot", "testbotOAuth", "channelToken", formatted_date, formatted_date)
        exists = dbconn.get_user(user.username)

        self.assertEqual(exists, None)
        dbconn.create_user(user)

        exists_now = dbconn.get_user(user.username)
        self.assertEqual(exists_now.username, user.username)
        self.cleanup()

    def test_verify_user(self):
        username = "normaltwitchuser@twitch.tv"
        password = "BobsYourUncle"
        dbconn = Db()

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        user = User(username, password, "testchannel", "testbot", "testbotOAuth", "channelToken", formatted_date,
                    formatted_date)
        dbconn.create_user(user)
        verified_user = dbconn.verify_user(user.username, user.password)

        dbconn.remove_user(user)
        self.assertEqual(user.username, verified_user.username)
        self.cleanup()

    def test_get_user(self):
        username = "normaltwitchuser@twitch.tv"
        dbconn = Db()

        now = datetime.now()
        now = now.replace(microsecond=0)
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        user = User(username, "userpassword", "testchannel", "testbot", "testbotOAuth", "channelToken", formatted_date,
                    formatted_date)
        dbconn.create_user(user)
        exists = dbconn.get_user(user.username)
        self.assertEqual(exists.created, now)

        self.cleanup()

    def test_remove_user(self):
        username = "normaltwitchuser@twitch.tv"
        dbconn = Db()

        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        user = User(username, "userpassword", "testchannel", "testbot", "testbotOAuth", "channelToken", formatted_date, formatted_date)
        exists = dbconn.get_user(user.username)
        self.assertEqual(exists, None)

        dbconn.create_user(user)
        exists_now = dbconn.get_user(user.username)
        self.assertEqual(exists_now.username, user.username)

        dbconn.remove_user(user)
        exists_after_delete = dbconn.get_user(user.username)
        self.assertEqual(exists_after_delete, None)

    def test_viewer_exists_in_db(self):
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        dbconn = Db()
        dbconn.create_viewer(twitchusername, channel, -1)

        res = dbconn.viewer_exists(twitchusername, channel)
        self.cleanup()

        self.assertEqual(res, True)

    def test_add_points(self):
        twitchusername = "IntegrationTestUser"
        points = 1000
        channel = "TestChannel"
        dbconn = Db()
        dbconn.create_viewer(twitchusername, channel, -1)

        current_points = dbconn.get_points(twitchusername, channel)
        expected_points = current_points + points
        dbconn.add_points(twitchusername, channel, points)
        new_points_total = dbconn.get_points(twitchusername, channel)
        self.cleanup()

        self.assertEqual(expected_points, new_points_total)

    def test_remove_points(self):
        twitchusername = "IntegrationTestUser"
        points = 1000
        channel = "TestChannel"
        dbconn = Db()
        dbconn.create_viewer(twitchusername, channel, -1)

        current_points = dbconn.get_points(twitchusername, channel)
        expected_points = current_points - points
        dbconn.remove_points(twitchusername, channel, points)
        new_points_total = dbconn.get_points(twitchusername, channel)

        self.cleanup()
        self.assertEqual(expected_points, new_points_total)

    def cleanup(self):
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        username = "normaltwitchuser@twitch.tv"
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        dbconn = Db()
        dbconn.remove_viewer(twitchusername, channel, -1)
        user = User(username, "userpassword", "testchannel", "testbot", "testbotOAuth", "channelToken", formatted_date,
                    formatted_date)
        dbconn.remove_user(user)

if __name__ == '__main__':
    unittest.main()





