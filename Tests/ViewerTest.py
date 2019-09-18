import unittest
import logging
from models.Viewer import Viewer

logging.basicConfig(level=logging.DEBUG)


class ViewerTest(unittest.TestCase):

    def test010_save(self):
        self.assertEqual(Viewer(10000, 'testviewer').exists(), None)
        Viewer(10000, 'testviewer').save()
        self.assertEqual(Viewer(10000, 'testviewer').exists(), True)

    def test020_exists(self):
        viewer = Viewer(10000, 'testviewer').load()
        exist_check = viewer.exists()
        self.assertEqual(exist_check, True)

    def test030_load(self):
        viewer = Viewer(10000, 'testviewer').load()
        self.assertIsNotNone(viewer)

    def test040_delete(self):
        viewer = Viewer(10000, 'testviewer').load()
        self.assertIsNotNone(viewer)
        viewer.delete()
        exist_check = viewer.exists()
        self.assertEqual(exist_check, None)
