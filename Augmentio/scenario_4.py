"""
Use the augmenter and add two types of augmentation to images and test1 how they will will look like
"""

from image_worker.augment import Augmenter
augmenter = Augmenter()
augmenter.specify_input_path('dataset/train/acinonyx-jubatus')
augmenter.do_additiveGuassianNoise_and_rotate()
augmenter.do_sharpen()
augmenter.run_view()
