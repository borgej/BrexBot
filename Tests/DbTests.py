import unittest
from Db import Db

class Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_user_exists_in_db(self):
        twitchusername = "bob"
        res = Db().viewer_exists(twitchusername)
        self.assertEqual(res, True)

    def test_add_points(self):
        twitchusername = "bob"
        points = 1000
        current_points = Db().get_points(twitchusername)
        expected_points = current_points + points
        Db().add_points(twitchusername, points)
        new_points_total = Db().get_points(twitchusername)
        self.assertEqual(expected_points, new_points_total)

    def test_remove_points(self):
        twitchusername = "bob"
        points = 1000
        current_points = Db().get_points(twitchusername)
        expected_points = current_points - points
        Db().remove_points(twitchusername, points)
        new_points_total = Db().get_points(twitchusername)
        self.assertEqual(expected_points, new_points_total)


if __name__ == '__main__':
    unittest.main()





