import unittest
import mysql.connector
from Db import Db

class Test(unittest.TestCase):
    def setup(self):
        # setup
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        dbconn = Db(database="brexbot", host="198.71.225.59", port=3306, user="brexbot", password="6Ke04_ij")
        dbconn.create_viewer(twitchusername, channel, -1)

    def test_user_exists_in_db(self):
        self.setup()
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        dbconn = Db(database="brexbot", host="198.71.225.59", port=3306, user="brexbot", password="6Ke04_ij")
        res = dbconn.viewer_exists(twitchusername, channel)
        self.cleanup()
        self.assertEqual(res, True)

    def test_add_points(self):
        self.setup()
        twitchusername = "IntegrationTestUser"
        points = 1000
        channel = "TestChannel"
        dbconn = Db(database="brexbot", host="198.71.225.59", port=3306, user="brexbot", password="6Ke04_ij")
        current_points = dbconn.get_points(twitchusername, channel)
        expected_points = current_points + points
        dbconn.add_points(twitchusername, channel, points)
        new_points_total = dbconn.get_points(twitchusername, channel)
        self.cleanup()
        self.assertEqual(expected_points, new_points_total)

    def test_remove_points(self):
        self.setup()
        twitchusername = "IntegrationTestUser"
        points = 1000
        channel = "TestChannel"
        dbconn = Db(database="brexbot", host="198.71.225.59", port=3306, user="brexbot", password="6Ke04_ij")
        current_points = dbconn.get_points(twitchusername, channel)
        expected_points = current_points - points
        dbconn.remove_points(twitchusername, channel, points)
        new_points_total = dbconn.get_points(twitchusername, channel)
        self.cleanup()
        self.assertEqual(expected_points, new_points_total)

    def cleanup(self):
        twitchusername = "IntegrationTestUser"
        channel = "TestChannel"
        dbconn = Db(database="brexbot", host="198.71.225.59", port=3306, user="brexbot", password="6Ke04_ij")
        dbconn.remove_viewer(twitchusername, channel, -1)

if __name__ == '__main__':
    unittest.main()





