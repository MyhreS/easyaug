"""
Using the augmenter class, augment the images in test folder using one or more augmenting types of your choice.
"""

from easyaug.augment import Augmenter
augmenter = Augmenter()
augmenter.specify_input_path("data/test")
augmenter.do_saltAndPepper()
augmenter.run_augment()


