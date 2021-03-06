import unittest
from unittest import mock

from easyaug.quickview import Quickviewer

class TestViewer(unittest.TestCase):
    def test_init(self):
        """Testing the init function"""
        viewer = Quickviewer()
        self.assertEqual(viewer.images, [])
        self.assertEqual(viewer.imagenames, [])

    def test_read_all_images(self):
        """Testing that the read_all_images function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_all_images('data/train')
        self.assertEqual(len(viewer.images), 5)

    def test_read_every_x_image(self):
        """Testing that the read_every_x_image function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_every_x_image('data/train', 2)
        self.assertEqual(len(viewer.images), 3)

    def test_read_first_x_images(self):
        """Testing that the read_first_x_images function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_first_x_images('data/train', 2)
        self.assertEqual(len(viewer.images), 2)

    def test_read_last_x_images(self):
        """Testing that the read_last_x_images function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_last_x_images('data/train', 2)
        self.assertEqual(len(viewer.images), 2)

    def test_read_a_image(self):
        """Testing that the read_a_image function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_a_image('data/train/panda/panda_0.jpg')
        self.assertEqual(len(viewer.images), 1)

    def test_read_all_imagenames(self):
        """Testing that the read_all_imagenames function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_all_imagenames('data/train')
        self.assertEqual(len(viewer.imagenames), 5)

    def test_read_every_x_imagename(self):
        """Testing that the read_every_x_imagename function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_every_x_imagename('data/train', 2)
        self.assertEqual(len(viewer.imagenames), 3)

    def test_read_first_x_imagenames(self):
        """Testing that the read_first_x_imagenames function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_first_x_imagenames('data/train', 2)
        self.assertEqual(len(viewer.imagenames), 2)

    def test_read_last_x_imagenames(self):
        """Testing that the read_last_x_imagenames function reads correct amount of images."""
        viewer = Quickviewer()
        viewer.read_last_x_imagenames('data/train', 2)
        self.assertEqual(len(viewer.imagenames), 2)

    @mock.patch('easyaug.quickview.view.view_images')
    def test_view_images(self, mock_view_augment):
        """Testing that the view_images function calls view_images."""
        viewer = Quickviewer()
        viewer.read_all_images('data/train')
        viewer.view_images()
        self.assertTrue(mock_view_augment.called)

    @mock.patch('easyaug.quickview.view.view_imagesnames')
    def test_view_imagenames(self, mock_view_augment):
        """Testing that the view_imagenames function calls view_imagesnames."""
        viewer = Quickviewer()
        viewer.read_all_imagenames('data/train')
        viewer.view_imagenames()
        self.assertTrue(mock_view_augment.called)

if __name__ == '__main__':
    unittest.main()