"""
Using processer resize your images to 256 format
"""

from image_worker.preprocess import Processer
processer = Processer()
processer.specify_input_and_output_path("dataset/train_little_augmented/acinonyx-jubatus_augmented", "dataset/acinonyx-jubatus_augmented_256")
processer.run_resize()

