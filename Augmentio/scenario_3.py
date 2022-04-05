"""
Scenario 3:
Quickly view the first 9 images from your folder to get an idea of what dataset you are working with.
"""
from image_worker.quickview import Quickviewer
viewer = Quickviewer()
viewer.read_first_x_images("dataset", 9)
viewer.view_images(9)
