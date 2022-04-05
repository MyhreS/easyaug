import os
import shutil
import unittest

import imageio.core

from image_worker.preprocess import Preprocesser

class test_processer(unittest.TestCase):
    def test_init(self):
        processer = Preprocesser()
        self.assertEqual(processer.input_path, None)
        self.assertEqual(processer.output_path, None)
        self.assertEqual(processer.type_of_image, None)

    def test_specify_input_and_output_path(self):
        processer = Preprocesser()
        processer.specify_input_and_output_path('data/train', 'data/train', 'jpg')
        self.assertEqual(processer.input_path, 'data/train')
        self.assertEqual(processer.output_path, 'data/train')
        self.assertEqual(processer.type_of_image, 'jpg')

    def test_resize(self):
        # make directory data/train_resized/panda_resized
        os.makedirs('data/train_resized/panda_resized', exist_ok=True)

        processer = Preprocesser()
        processer.specify_input_and_output_path('data/train/panda', 'data/train_resized/panda_resized')
        processer.run_resize((100, 100))

        # Read new image and check if it is resized
        image = imageio.imread('data/train_resized/panda_resized/panda_0.jpg')
        self.assertEqual(image.shape, (100, 100, 3))

        # Remove directory data/train_resized that it was created.
        shutil.rmtree('data/train_resized')


if __name__ == '__main__':
    unittest.main()