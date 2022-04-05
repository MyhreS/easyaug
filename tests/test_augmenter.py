"""Tests the augment module."""
import glob
import os
import shutil
import unittest
from unittest import mock
import imageio
import numpy as np
from imgaug import augmenters as iaa

from easyaug.augment import Augmenter

# Write test for the Augmenter class here.
class TestAugmenter(unittest.TestCase):
    """Tests the Augmenter class."""

    def test_init(self):
        """Tests that the class is initialized correctly."""

        augmenter = Augmenter()
        self.assertEqual(augmenter.input_path, None)
        self.assertEqual(augmenter.output_path, None)
        self.assertEqual(augmenter.type_of_image, None)
        self.assertEqual(augmenter.augmentation_todo, iaa.Sequential())
        self.assertEqual(augmenter.todo_names, [])

    def test_specify_input_path_1(self):
        """Tests that the input_path set by specify_path method is correct."""
        augmenter = Augmenter()
        augmenter.specify_input_path('easyaug/tests/data/train')
        self.assertEqual(augmenter.input_path, 'easyaug/tests/data/train')

    def test_specify_input_path_2(self):
        """Tests that the type_of_image set by specify_path method is correct."""
        augmenter = Augmenter()
        augmenter.specify_input_path('easyaug/tests/data/train', 'png')
        self.assertEqual(augmenter.type_of_image, 'png')


    def test_specify_output_path(self):
        """Tests that the output_path set by specify_path method is correct."""
        augmenter = Augmenter()
        augmenter.specify_output_path('easyaug/tests/data/train_output')
        self.assertEqual(augmenter.output_path, 'easyaug/tests/data/train_output')

    def test_do_guassianBlur_1(self):
        """Tests that the guassian blur is added to augmentation_todo list by the do_guassianBlur method."""
        augmenter = Augmenter()
        augmenter.do_gaussianBlur(1.0, 3.0)
        guassian_blur = iaa.GaussianBlur(sigma=(1.0, 3.0))

        # If the type of the augmentation is not the same as the type of the guassian blur, then the test fails.
        if type(augmenter.augmentation_todo[0])==type(guassian_blur):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_guassianBlur_2(self):
        """Tests that 'Guassian Blur' is added to todo_names list by the do_guassianBlur method."""
        augmenter = Augmenter()
        augmenter.do_gaussianBlur(1.0, 3.0)

        # If the first todo name is not 'Gaussian Blur', then the test fails.
        if augmenter.todo_names[0] == 'Gaussian Blur':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_sharpen_1(self):
        """Tests that the sharpen is added to augmentation_todo list by the do_Sharpen method."""
        augmenter = Augmenter()
        augmenter.do_sharpen(0.15,0.6)
        sharpen = iaa.Sharpen(0.15, 0.6)

        # If the type of the augmentation is not the same as the type of the sharpen, then the test fails.
        if type(augmenter.augmentation_todo[0])==type(sharpen):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_sharpen_2(self):
        """Tests that 'Sharpen' is added to todo_names list by the do_Sharpen method."""
        augmenter = Augmenter()
        augmenter.do_sharpen(0.15, 0.6)

        # If the first todo name is not 'Sharpen', then the test fails.
        if augmenter.todo_names[0] == 'Sharpen':
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    def test_do_saltAndPepper(self):
        """Tests that the saltAndPepper is added to augmentation_todo list by the do_saltAndPepper method."""
        augmenter = Augmenter()
        augmenter.do_saltAndPepper(0.15, 0.6)
        saltAndPepper = iaa.SaltAndPepper((0.15, 0.6))

        # If the type of the augmentation is not the same as the type of the saltAndPepper, then the test fails.
        if type(augmenter.augmentation_todo[0])==type(saltAndPepper):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_saltAndPepper_2(self):
        """Tests that 'Salt and Pepper' is added to todo_names list by the do_saltAndPepper method."""
        augmenter = Augmenter()
        augmenter.do_saltAndPepper(0.15, 0.6)

        # If the first todo name is not 'Salt and Pepper', then the test fails.
        if augmenter.todo_names[0] == 'Salt and Pepper':
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    def test_do_additiveGaussianNoise_1(self):
        """Tests that the additiveGaussianNoise is added to augmentation_todo list by the do_additiveGaussianNoise method."""
        augmenter = Augmenter()
        augmenter.do_additiveGaussianNoise(10, 40)
        additiveGuassianNoise = iaa.AdditiveGaussianNoise(scale=(10, 40))

        # If the type of the augmentation is not the same as the type of the additiveGuassianNoise, then the test fails.
        if type(augmenter.augmentation_todo[0])==type(additiveGuassianNoise):
            self.assertTrue(True)
        else:
            self.assertTrue(False)


    def test_do_additiveGuassianNoise_2(self):
        """Tests that 'Additive Gaussian Noise' is added to todo_names list by the do_additiveGaussianNoise method."""
        augmenter = Augmenter()
        augmenter.do_additiveGaussianNoise(10, 40)

        # If the first todo name is not 'Additive Gaussian Noise', then the test fails.
        if augmenter.todo_names[0] == 'Additive Gaussian Noise':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_rotate_1(self):
        """Tests that the rotate is added to augmentation_todo list by the do_rotate method."""
        augmenter = Augmenter()
        augmenter.do_rotate(90, 90)
        rotate = iaa.Rotate((-90, 90))

        # If the type of the augmentation is not the same as the type of the rotate, then the test fails.
        if type(augmenter.augmentation_todo[0])==type(rotate):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_rotate_2(self):
        """Tests that 'Rotate' is added to todo_names list by the do_rotate method."""
        augmenter = Augmenter()
        augmenter.do_rotate(90, 90)

        # If the first todo name is not 'Rotate', then the test fails.
        if augmenter.todo_names[0] == 'Rotate':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_pad_1(self):
        """Tests that the pad is added to augmentation_todo list by the do_pad method."""
        augmenter = Augmenter()
        augmenter.do_pad(10, 10, 10, 10)
        pad = iaa.Pad(px=(10, 10, 10, 10))

        # If the type of the augmentation is not the same as the type of the pad, then the test fails.
        if type(augmenter.augmentation_todo[0])==type(pad):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_pad_2(self):
        """Tests that 'Pad' is added to todo_names list by the do_pad method."""
        augmenter = Augmenter()
        augmenter.do_pad(10, 10, 10, 10)

        # If the first todo name is not 'Pad', then the test fails.
        if augmenter.todo_names[0] == 'Pad':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_scale(self):
        """Tests that the scale is added to augmentation_todo list by the do_scale method."""
        augmenter = Augmenter()
        augmenter.do_scale(0.2, 2.0)
        scale = iaa.Affine(scale=(0.2, 2.0))

        # If the type of the augmentation is not the same as the type of the scale, then the test fails.
        if type(augmenter.augmentation_todo[0])==type(scale):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_scale_2(self):
        """Tests that 'Scale' is added to todo_names list by the do_scale method."""
        augmenter = Augmenter()
        augmenter.do_scale(0.2, 2.0)

        # If the first todo name is not 'Scale', then the test fails.
        if augmenter.todo_names[0] == 'Scale':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_guassianBlur_and_rotate_1(self):
        """Tests that the gaussian blur and rotate are added in sequential to augmentation_todo list by the do_gaussianBlur_and_rotate method."""
        augmenter = Augmenter()
        augmenter.do_gaussianBlur_and_rotate(0.2, 3.2, 90, 90)
        sequential = iaa.Sequential()
        sequential.add(iaa.GaussianBlur(sigma=(0.2, 3.2)))
        sequential.add(iaa.Rotate((-90, 90)))
        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_guassianBlur_and_rotate_2(self):
        """Tests that 'Gaussian Blur and Rotate' are added to todo_names list by the do_gaussianBlur_and_rotate method."""
        augmenter = Augmenter()
        augmenter.do_gaussianBlur_and_rotate(0.2, 3.2, 90, 90)

        # If the first todo name is not 'Gaussian Blur and Rotate', then the test fails.
        if augmenter.todo_names[0] == 'Gaussian Blur and Rotate':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_guassianBlur_and_pad(self):
        """Tests that the guassian blur and pad are added in sequential to augmentation_todo list by the do_gaussianBlur_and_pad method."""
        augmenter = Augmenter()
        augmenter.do_gaussianBlur_and_pad(0.5, 3.0, 10, 10, 10, 10)
        sequential = iaa.Sequential()
        sequential.add(iaa.GaussianBlur(sigma=(0.5, 3.0)))
        sequential.add(iaa.Pad(px=(10, 10, 10, 10)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_guassianBlur_and_pad_2(self):
        """Tests that 'Guassian Blur and Pad' are added to todo_names list by the do_gaussianBlur_and_pad method."""
        augmenter = Augmenter()
        augmenter.do_gaussianBlur_and_pad(0.5, 3.0, 10, 10, 10, 10)

        # If the first todo name is not 'Gaussian Blur and Pad', then the test fails.
        if augmenter.todo_names[0] == 'Gaussian Blur and Pad':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_guassianBlur_and_scale_1(self):
        """Tests that the guassian blur and scale are added in sequential to augmentation_todo list by the do_gaussianBlur_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_gaussianBlur_and_scale(0.5, 3.0, 0.2, 2.0)
        sequential = iaa.Sequential()
        sequential.add(iaa.GaussianBlur(sigma=(0.5, 3.0)))
        sequential.add(iaa.Affine(scale=(0.2, 2.0)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_guassianBlur_and_scale_2(self):
        """Tests that 'Guassian Blur and Scale' are added to todo_names list by the do_gaussianBlur_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_gaussianBlur_and_scale(0.5, 3.0, 0.2, 2.0)

        # If the first todo name is not 'Gaussian Blur and Scale', then the test fails.
        if augmenter.todo_names[0] == 'Gaussian Blur and Scale':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_rotate_and_scale_1(self):
        """Tests that the rotate and scale are added in sequential to augmentation_todo list by the do_rotate_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_rotate_and_scale(180, 180, 0.5, 1.5)
        sequential = iaa.Sequential()
        sequential.add(iaa.Rotate((-180, 180)))
        sequential.add(iaa.Affine(scale=(0.5, 1.5)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_rotate_and_scale_2(self):
        """Tests that 'Rotate and Scale' are added to todo_names list by the do_rotate_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_rotate_and_scale(180, 180, 0.5, 1.5)

        # If the first todo name is not 'Rotate and Scale', then the test fails.
        if augmenter.todo_names[0] == 'Rotate and Scale':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_sharpen_and_rotate_1(self):
        """Tests that the sharpen and rotate are added in sequential to augmentation_todo list by the do_sharpen_and_rotate method."""
        augmenter = Augmenter()
        augmenter.do_sharpen_and_rotate(0.1, 0.5, 180, 180)
        sequential = iaa.Sequential()
        sequential.add(iaa.Sharpen(0.1, 0.5))
        sequential.add(iaa.Rotate((-180, 180)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_sharpen_and_rotate_2(self):
        """Tests that 'Sharpen and Rotate' are added to todo_names list by the do_sharpen_and_rotate method."""
        augmenter = Augmenter()
        augmenter.do_sharpen_and_rotate(0.1, 0.5, 180, 180)

        # If the first todo name is not 'Sharpen and Rotate', then the test fails.
        if augmenter.todo_names[0] == 'Sharpen and Rotate':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_sharpen_and_pad_1(self):
        """Tests that the sharpen and pad are added in sequential to augmentation_todo list by the do_sharpen_and_pad method."""
        augmenter = Augmenter()
        augmenter.do_sharpen_and_pad(0.1, 0.5, 10, 10, 10, 10)
        sequential = iaa.Sequential()
        sequential.add(iaa.Sharpen(0.1, 0.5))
        sequential.add(iaa.Pad(px=(10, 10, 10, 10)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_sharpen_and_pad_2(self):
        """Tests that 'Sharpen and Pad' are added to todo_names list by the do_sharpen_and_pad method."""
        augmenter = Augmenter()
        augmenter.do_sharpen_and_pad(0.1, 0.5, 10, 10, 10, 10)

        # If the first todo name is not 'Sharpen and Pad', then the test fails.
        if augmenter.todo_names[0] == 'Sharpen and Pad':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_sharpen_and_scale_1(self):
        """Tests that the sharpen and scale are added in sequential to augmentation_todo list by the do_sharpen_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_sharpen_and_scale(0.1, 0.5, 0.5, 1.5)
        sequential = iaa.Sequential()
        sequential.add(iaa.Sharpen(0.1, 0.5))
        sequential.add(iaa.Affine(scale=(0.5, 1.5)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_sharpen_and_scale_2(self):
        """Tests that 'Sharpen and Scale' are added to todo_names list by the do_sharpen_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_sharpen_and_scale(0.1, 0.5, 0.5, 1.5)

        # If the first todo name is not 'Sharpen and Scale', then the test fails.
        if augmenter.todo_names[0] == 'Sharpen and Scale':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_saltAndPepper_and_rotate_1(self):
        """Tests that the salt and pepper and rotate are added in sequential to augmentation_todo list by the do_saltAndPepper_and_rotate method."""
        augmenter = Augmenter()
        augmenter.do_saltAndPepper_and_rotate(0.1, 0.5, 180, 180)
        sequential = iaa.Sequential()
        sequential.add(iaa.SaltAndPepper((0.1, 0.5)))
        sequential.add(iaa.Rotate((-180, 180)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_saltAndPepper_and_rotate_2(self):
        """Tests that 'Salt and Pepper and Rotate' are added to todo_names list by the do_saltAndPepper_and_rotate method."""
        augmenter = Augmenter()
        augmenter.do_saltAndPepper_and_rotate(0.1, 0.5, 180, 180)

        # If the first todo name is not 'Salt and Pepper and Rotate' then the test fails.
        if augmenter.todo_names[0] == 'Salt and Pepper and Rotate':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_saltAndPepper_and_pad_1(self):
        """Tests that the salt and pepper and pad are added in sequential to augmentation_todo list by the do_saltAndPepper_and_pad method."""
        augmenter = Augmenter()
        augmenter.do_saltAndPepper_and_pad(0.1, 0.5, 10, 10, 10, 10)
        sequential = iaa.Sequential()
        sequential.add(iaa.SaltAndPepper((0.1, 0.5)))
        sequential.add(iaa.Pad(px=(10, 10, 10, 10)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_saltAndPepper_and_pad_2(self):
        """Tests that 'Salt and Pepper and Pad' are added to todo_names list by the do_saltAndPepper_and_pad method."""
        augmenter = Augmenter()
        augmenter.do_saltAndPepper_and_pad(0.1, 0.5, 10, 10, 10, 10)

        # If the first todo name is not 'Salt and Pepper and Pad', then the test fails.
        if augmenter.todo_names[0] == 'Salt and Pepper and Pad':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_saltAndPepper_and_scale_1(self):
        """Tests that the salt and pepper and scale are added in sequential to augmentation_todo list by the do_saltAndPepper_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_saltAndPepper_and_scale(0.1, 0.5, 0.5, 1.5)
        sequential = iaa.Sequential()
        sequential.add(iaa.SaltAndPepper((0.1, 0.5)))
        sequential.add(iaa.Affine(scale=(0.5, 1.5)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_saltAndPepper_and_scale_2(self):
        """Tests that 'Salt and Pepper and Scale' are added to todo_names list by the do_saltAndPepper_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_saltAndPepper_and_scale(0.1, 0.5, 0.5, 1.5)

        # If the first todo name is not 'Salt and Pepper and Scale', then the test fails.
        if augmenter.todo_names[0] == 'Salt and Pepper and Scale':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_additiveGuassianNoise_and_rotate_1(self):
        """Tests that the additive guassian noise and rotate are added in sequential to augmentation_todo list by the do_additiveGuassianNoise_and_rotate method."""
        augmenter = Augmenter()
        augmenter.do_additiveGuassianNoise_and_rotate(10, 40, 180, 180)
        sequential = iaa.Sequential()
        sequential.add(iaa.AdditiveGaussianNoise(scale=(10, 40)))
        sequential.add(iaa.Rotate((-180, 180)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_additiveGuassianNoise_and_rotate_2(self):
        """Tests that 'Additive Guassian Noise and Rotate' are added to todo_names list by the do_additiveGuassianNoise_and_rotate method."""
        augmenter = Augmenter()
        augmenter.do_additiveGuassianNoise_and_rotate(10, 40, 180, 180)

        # If the first todo name is not 'Additive Guassian Noise and Rotate', then the test fails.
        if augmenter.todo_names[0] == 'Additive Guassian Noise and Rotate':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_additiveGuassianNoise_and_pad_1(self):
        """Tests that the additive guassian noise and pad are added in sequential to augmentation_todo list by the do_additiveGuassianNoise_and_pad method."""
        augmenter = Augmenter()
        augmenter.do_additiveGuassianNoise_and_pad(10, 40, 10, 10, 10, 10)
        sequential = iaa.Sequential()
        sequential.add(iaa.AdditiveGaussianNoise(scale=(10, 40)))
        sequential.add(iaa.Pad(px=(10, 10, 10, 10)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_additiveGuassianNoise_and_pad_2(self):
        """Tests that 'Additive Guassian Noise and Pad' are added to todo_names list by the do_additiveGuassianNoise_and_pad method."""
        augmenter = Augmenter()
        augmenter.do_additiveGuassianNoise_and_pad(10, 40, 10, 10, 10, 10)

        # If the first todo name is not 'Additive Guassian Noise and Pad', then the test fails.
        if augmenter.todo_names[0] == 'Additive Guassian Noise and Pad':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_do_additiveGuassianNoise_and_scale_1(self):
        """Tests that the additive guassian noise and scale are added in sequential to augmentation_todo list by the do_additiveGuassianNoise_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_additiveGuassianNoise_and_scale(10, 40, 0.5, 1.5)
        sequential = iaa.Sequential()
        sequential.add(iaa.AdditiveGaussianNoise(scale=(10, 40)))
        sequential.add(iaa.Affine(scale=(0.5, 1.5)))

        passes = True
        passes = self.multi_augmentation(augmenter, passes, sequential)
        self.assertTrue(passes)

    def test_do_additiveGuassianNoise_and_scale_2(self):
        """Tests that 'Additive Guassian Noise and Scale' are added to todo_names list by the do_additiveGuassianNoise_and_scale method."""
        augmenter = Augmenter()
        augmenter.do_additiveGuassianNoise_and_scale(10, 40, 0.5, 1.5)

        # If the first todo name is not 'Additive Guassian Noise and Scale', then the test fails.
        if augmenter.todo_names[0] == 'Additive Guassian Noise and Scale':
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def multi_augmentation(self, augmenter, passes, sequential):
        """ Check if multiple augmentation types is added to the augmentation_todo in a sequential list."""
        if type(augmenter.augmentation_todo[0]) == type(sequential):
            for aug_type_todo, aug_type_seq in zip(augmenter.augmentation_todo[0], sequential):
                if type(aug_type_todo) != type(aug_type_seq):
                    passes = False
        else:
            passes = False
        return passes


    @mock.patch('easyaug.augment.run_view.view_augment')
    def test_run_view(self, mock_view_augment):
        """Tests that the run_view() method calls the view_augment() method."""
        augmenter = Augmenter()
        augmenter.specify_input_path('easyaug/tests/data/train')
        augmenter.do_rotate(10, 10)
        augmenter.run_view()
        self.assertTrue(mock_view_augment.called)

    def test_run_augment(self):
        """Testing that the run_augment using all augmentation_types is augmenting it correctly."""

        # Running all augmentation types.
        augmenter = Augmenter()
        augmenter.specify_input_path('data/train')
        augmenter.do_gaussianBlur(0.5, 3.0)
        augmenter.do_sharpen(0.1, 0.5)
        augmenter.do_saltAndPepper(0.1, 0.5)
        augmenter.do_additiveGaussianNoise(5, 50)
        augmenter.do_rotate(180, 180)
        augmenter.do_pad(20, 20, 20, 20)
        augmenter.do_scale(0.5, 1.5)
        augmenter.do_gaussianBlur_and_rotate(0.5, 3.0, 180, 180)
        augmenter.do_gaussianBlur_and_pad(0.5, 3.0, 20, 20, 20, 20)
        augmenter.do_gaussianBlur_and_scale(0.5, 3.0, 0.5, 1.5)
        augmenter.do_rotate_and_scale(180, 180, 0.5, 1.5)
        augmenter.do_sharpen_and_rotate(0.1, 0.5, 180, 180)
        augmenter.do_sharpen_and_pad(0.1, 0.5, 20, 20, 20, 20)
        augmenter.do_sharpen_and_scale(0.1, 0.5, 0.5, 1.5)
        augmenter.do_saltAndPepper_and_rotate(0.1, 0.5, 180, 180)
        augmenter.do_saltAndPepper_and_pad(0.1, 0.5, 20, 20, 20, 20)
        augmenter.do_saltAndPepper_and_scale(0.1, 0.5, 0.5, 1.5)
        augmenter.do_additiveGuassianNoise_and_rotate(5, 50, 180, 180)
        augmenter.do_additiveGuassianNoise_and_pad(5, 50, 20, 20, 20, 20)
        augmenter.do_additiveGuassianNoise_and_scale(5, 50, 0.5, 1.5)
        augmenter.run_augment()

        # Checking if data/train_augmented folder is created.
        self.assertEqual(os.path.exists('data/train_augmented'), True)

        # Checking if panda_augmented folder is created.
        self.assertEqual(os.path.exists('data/train_augmented/panda_augmented'), True)

        # Checking if the data/train_augmented folder contains correct amount of images.
        panda_augmented_files = glob.glob('data/train_augmented/panda_augmented/*')
        self.assertEqual(len(panda_augmented_files) == len(augmenter.augmentation_todo)+1, True)

        # Checking if each image is not equal to the original image.
        panda_0 = imageio.imread('data/train/panda/panda_0.jpg')
        # Removing the panda_0.jpg from the list of files.
        panda_augmented_files.remove('data/train_augmented/panda_augmented\\panda_0.jpg')
        for image_path in panda_augmented_files:
            image = imageio.imread(image_path)
            # Checking if the image is not equal to the original image.
            self.assertNotEqual(np.array_equal(image, panda_0), True)

        # Removing the data/train_augmented folder that it created.
        shutil.rmtree('data/train_augmented')


if __name__ == '__main__':
    unittest.main()