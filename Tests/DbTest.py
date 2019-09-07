import unittest
import mysql.connector
from Db import Db

class Test(unittest.TestCase):
    def test_setup(self):
        # setup
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        Db().create_viewer(twitchusername, channel, -1)

    def test_user_exists_in_db(self):
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        res = Db().viewer_exists(twitchusername, channel)
        self.assertEqual(res, True)

    def test_add_points(self):
        twitchusername = "IntegrationTestUser"
        points = 1000
        channel = "TestChannel"
        current_points = Db().get_points(twitchusername, channel)
        expected_points = current_points + points
        Db().add_points(twitchusername, channel, points)
        new_points_total = Db().get_points(twitchusername, channel)
        self.assertEqual(expected_points, new_points_total)

    def test_remove_points(self):
        twitchusername = "IntegrationTestUser"
        points = 1000
        channel = "TestChannel"
        current_points = Db().get_points(twitchusername, channel)
        expected_points = current_points - points
        Db().remove_points(twitchusername, channel, points)
        new_points_total = Db().get_points(twitchusername, channel)
        self.assertEqual(expected_points, new_points_total)

    def test_cleanup_remove_viewer(self):
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        Db().remove_viewer(channel, twitchusername, -1)

if __name__ == '__main__':
    unittest.main()





