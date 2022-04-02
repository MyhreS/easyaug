"""Tests the augment module."""

import unittest
import numpy as np
from imgaug import augmenters as iaa

from image_worker.augment import Augmenter

# Write test for the Augmenter class here.
class TestAugmenter(unittest.TestCase):
    """Tests the Augmenter class."""

    def test_specify_input_path_true(self):
        """Tests the specify_path method."""
        augmenter = Augmenter()
        augmenter.specify_input_path('image_worker/tests/data/train', 'png')
        if
        self.assertEqual(augmenter.input_path, 'image_worker/tests/data/train')
        self.assertEqual(augmenter.type_of_image, 'png')


    def test_specify_output_path(self):
        """Tests the specify_path method."""
        augmenter = Augmenter()
        augmenter.specify_output_path('image_worker/tests/data/train_output')
        self.assertEqual(augmenter.output_path, 'image_worker/tests/data/train_output')

    def test_do_guassian_blur(self):
        """Tests the do_guassian_blur method."""
        fails = False
        augmenter = Augmenter()
        augmenter.do_gaussianBlur(1.0,3.0)
        guassian_blur = iaa.GaussianBlur(sigma=(1.0, 3.0))

        # If the type of the augmentation is not the same as the type of the guassian blur, then the test fails.
        if type(augmenter.augmentation_todo[0])!=type(guassian_blur):
            self.assertTrue(False)
        # If the first todo name is not 'Gaussian Blur', then the test fails.
        if augmenter.todo_names[0]!='Gaussian Blur':
            self.assertTrue(False)
        self.assertTrue(True)












if __name__ == '__main__':
    unittest.main()

    """
    def test_augment_image(self):
        #Tests the augment_image method
        # Create an Augmenter object.
        augmenter = Augmenter()
        # Create a test image.
        image = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        # Augment the image.
        augmented_image = augmenter.augment_image(image)
        # Check that the image was augmented.
        self.assertNotEqual(image, augmented_image)
        # Check that the image was rotated.
        self.assertNotEqual(image[0, 0], augmented_image[0, 0])
        # Check that the image was flipped.
        self.assertNotEqual(image[0, 1], augmented_image[0, 1])
        # Check that the image was translated.
        self.assertNotEqual(image[1, 0], augmented_image[1, 0])
        # Check that the image was scaled.
        self.assertNotEqual(image[1, 1], augmented_image[1, 1])
        # Check that the image was sheared.
        self.assertNotEqual(image[2, 0], augmented_image[2, 0])
        # Check that the image was rotated and translated.
        self.assertNotEqual(image[1, 1], augmented_image[1, 1])
        # Check that the image was rotated and flipped.
        self.assertNotEqual(image[2, 2], augmented_image[2, 2])
        # Check that the image was flipped and translated.
        self.assertNotEqual(image[2, 1], augmented_image[2, 1])
        # Check that the image was translated and scaled.
        self.assertNotEqual(image[0, 2], augmented_image[0, 2])
        # Check that the image was rotated, flipped and translated.
        self.assertNotEqual(image[2, 2], augmented_image[2, 2])
        # Check that the image was rotated, flipped, translated and scaled
    """