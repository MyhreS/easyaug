"""
Using the augmenter class, augment the images in acinonyx-jubatus using one or more augmenting types of your choice.
"""

from easyaug.augment import Augmenter
augmenter = Augmenter()
augmenter.specify_input_path("easyaug/tests/data/train")
augmenter.specify_output_path("dataset/train_little_augmented")
augmenter.do_saltAndPepper()
augmenter.run_augment()


