"""
Scenario 7:
Using processer resize the images in data/test/panda to 256 format and place the in the data/resized folder.
"""

from easyaug.preprocess import Preprocesser
processer = Preprocesser()
processer.specify_input_and_output_path("data/test/panda", "data/resized_folder")
processer.run_resize((256, 256))

