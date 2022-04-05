import glob
import math
import unittest
from image_worker.quickview import Viewer

class TestViewer(unittest.TestCase):
    def test_init(self):
        """Testing the init function"""
        viewer = Viewer()
        self.assertEqual(viewer.images, [])
        self.assertEqual(viewer.imagenames, [])

    def test_read_all_images(self):
        """Testing that the read_all_images function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_all_images('data/test')
        self.assertEqual(len(viewer.images), 5)

    def test_read_every_x_image(self):
        """Testing that the read_every_x_image function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_every_x_image('data/test', 2)
        self.assertEqual(len(viewer.images), 3)

    def test_read_first_x_images(self):
        """Testing that the read_first_x_images function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_first_x_images('data/test', 2)
        self.assertEqual(len(viewer.images), 2)

    def test_read_last_x_images(self):
        """Testing that the read_last_x_images function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_last_x_images('data/test', 2)
        self.assertEqual(len(viewer.images), 2)

    def test_read_a_image(self):
        """Testing that the read_a_image function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_a_image('data/test/panda/panda_0.jpg')
        self.assertEqual(len(viewer.images), 1)

    def test_read_all_imagenames(self):
        """Testing that the read_all_imagenames function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_all_imagenames('data/test')
        self.assertEqual(len(viewer.imagenames), 5)

    def test_read_every_x_imagename(self):
        """Testing that the read_every_x_imagename function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_every_x_imagename('data/test', 2)
        self.assertEqual(len(viewer.imagenames), 3)

    def test_read_first_x_imagenames(self):
        """Testing that the read_first_x_imagenames function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_first_x_imagenames('data/test', 2)
        self.assertEqual(len(viewer.imagenames), 2)

    def test_read_last_x_imagenames(self):
        """Testing that the read_last_x_imagenames function reads correct amount of images."""
        viewer = Viewer()
        viewer.read_last_x_imagenames('data/test', 2)
        self.assertEqual(len(viewer.imagenames), 2)






if __name__ == '__main__':
    unittest.main()