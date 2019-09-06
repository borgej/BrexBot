import unittest
import Db

class Test(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_user_exists_in_db(self):
        user = "bob"
        res = Db.viewer_exists(user)
        self.assertEqual(res, True)




if __name__ == '__main__':
    unittest.main()





