"""
Scenario 3:
Quickly view the first 10 images from your folder to get an idea of what dataset you are working with.
"""

from image_worker import quickview
viewer = quickview.Viewer()
result = viewer.read_last_x_imagenames("dataset", 10)
print(len(result))

#viewer.read_a_image("dataset/train/acinonyx-jubatus/acinonyx-jubatus_0_052c1ab2.jpg")
