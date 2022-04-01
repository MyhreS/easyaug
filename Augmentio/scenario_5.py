"""
Using the augmenter class, augment the images in acinonyx-jubatus using one or more augmenting types of your choice.
"""

from image_worker.augment import Augmenter
augmenter = Augmenter()
#augmenter.specify_path("dataset/train_little/acinonyx-jubatus")
augmenter.specify_path("dataset/train_little/", "PNG")
augmenter.do_saltAndPepper()
augmenter.run_augment()

