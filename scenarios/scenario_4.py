"""
Scenario 4:
Quickly view the first 2 images from your folder to get an idea of what dataset you are working with.
"""
from easyaug.quickview import Quickviewer
viewer = Quickviewer()
viewer.read_first_x_images("data/train", 2)
viewer.view_images()
