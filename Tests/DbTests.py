import unittest
import mysql.connector
from Db import Db

class Test(unittest.TestCase):
    def setup(self):
        # setup
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        self.db.create_viewer(twitchusername, channel, -1)
        self.assertEqual(True, True)

    def user_exists_in_db(self):
        twitchusername = "IntegrationTestUser"
        res = Db().viewer_exists(twitchusername)
        self.assertEqual(res, True)

    def add_points(self):
        twitchusername = "IntegrationTestUser"
        points = 1000

        current_points = Db().get_points(twitchusername)
        expected_points = current_points + points
        Db().add_points(twitchusername, points)
        new_points_total = Db().get_points(twitchusername)
        self.assertEqual(expected_points, new_points_total)

    def remove_points(self):
        twitchusername = "IntegrationTestUser"
        points = 1000

        current_points = Db().get_points(twitchusername)
        expected_points = current_points - points
        Db().remove_points(twitchusername, points)
        new_points_total = Db().get_points(twitchusername)
        self.assertEqual(expected_points, new_points_total)

    def cleanup_remove_viewer(self):
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        Db().remove_viewer(twitchusername, channel, -1)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()





