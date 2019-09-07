import unittest
from Db import Db


class Test(unittest.TestCase):
    def test_user_exists_in_db(self):
        twitchusername = "bob"
        res = Db().viewer_exists(twitchusername)
        self.assertEqual(res, True)

    def test_add_points(self):
        twitchusername = "bob"
        points = 100
        res = Db().add_points(twitchusername, points)
        self.assertEqual(res, True)

    def test_remove_points(self):
        twitchusername = "bob"
        points = 100
        res = Db().remove_points(twitchusername, points)
        self.assertEqual(res, True)

if __name__ == '__main__':
    unittest.main()





