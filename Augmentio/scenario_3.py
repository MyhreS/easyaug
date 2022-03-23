"""
Scenario 3:
Quickly view the 10 images from your folder to get an idea of what you are working with.
"""

from image_worker import quickview
viewer = quickview.Viewer()

viewer.read_all_images()