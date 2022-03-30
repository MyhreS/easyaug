"""
Use the augmenter and add two types of augmentation to images and test how they will will look like
"""

from image_worker.augment import Augmenter
augmenter = Augmenter()
augmenter.specify_path('dataset/train/acinonyx-jubatus')
#augmenter.do_gaussianBlur()
#augmenter.do_rotate()
#augmenter.do_guassianBlur_and_rotation()
#augmenter.do_pad()
#augmenter.do_scale()
#augmenter.do_sharpen()
#augmenter.do_saltAndPepper()
#augmenter.do_additiveGuassianNoise()
augmenter.do_additiveGuassianNoise_and_rotate()
augmenter.run_view()
