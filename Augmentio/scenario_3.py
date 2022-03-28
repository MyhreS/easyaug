"""
Scenario 3:
Quickly view the first 9 images from your folder to get an idea of what dataset you are working with.
"""
from image_worker.quickview import Viewer
viewer = Viewer()
viewer.read_first_x_images("dataset", 9)
viewer.view_images(9)
