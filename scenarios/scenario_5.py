"""
Use the augmenter and add two types of augmentation to images and test how they will will look like
"""

from easyaug.augment import Augmenter
augmenter = Augmenter()
augmenter.specify_input_path('data/train')
augmenter.do_additiveGuassianNoise_and_rotate()
augmenter.do_sharpen()
augmenter.run_view()
