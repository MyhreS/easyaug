"""
Use the augmenter and add two types of augmentation to images and test how they will will look like
"""

from image_worker.augment import Augmenter
augmenter = Augmenter()
augmenter.specify_path('dataset/train/acinonyx-jubatus')
augmenter.do_gaussianBlur(0, 3)
augmenter.run_view()
