"""
Using processer resize your images to 256 format
"""

from image_worker.preprocess import Preprocesser
processer = Preprocesser()
processer.specify_input_and_output_path("dataset/train_little_augmented/acinonyx-jubatus_augmented", "dataset/acinonyx-jubatus_augmented_256")
processer.run_resize()

