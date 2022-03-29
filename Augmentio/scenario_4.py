"""
Use the augmenter and add two types of augmentation to images and test how they will will look like
"""

from image_worker.augment import Augmenter
augmenter = Augmenter()
augmenter.specify_path('dataset/train/acinonyx-jubatus')
#augmenter.do_gaussianBlur(0, 3)
#augmenter.do_rotation(0, 30)
#augmenter.do_guassianBlur_and_rotation(0, 3, 0, 30)
#augmenter.do_pad()
#augmenter.do_scale(0.5)
augmenter.run_view()
