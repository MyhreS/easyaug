# An example
An example of viewing, preparing and augmenting a dataset.

Installing the framework
```bash
pip install easyaug
```

## Quickview
Quicky viewing all images in the 'data' folder
```python
from easyaug.quickview import Quickviewer

quickviewer = Quickviewer()
quickviewer.read_all_images('data')
quickviewer.view_images()
```
## Preprocess
The preprocesser is simple so the directories has to be created manually unlike the two other packages.
```python
# Resizing the images to 256x256
from easyaug.preprocess import Preprocesser
preprocesser = Preprocesser()
# First for the training folder.
preprocesser.specify_input_and_output_path('data/train/panda', 'data_resized/train_resized/panda_resized')
preprocesser.run_resize((256, 256))
# Then for the test folder.
preprocesser.specify_input_and_output_path('data/test/panda', 'data_resized/test_resized/panda_resized')
preprocesser.run_resize((256, 256))
```

## Augment
Easily augmenting the images in the 'data' folder with rotate and pad. First checks that it is what I want
```python
# Testing first
from easyaug.augment import Augmenter
augmenter = Augmenter()
augmenter.specify_input_path('data_resized')
augmenter.do_rotate()
augmenter.do_pad(5, 5, 20, 20) # Specified the parameters to show parameter tuning.
augmenter.run_view()
```
Then running the augmentation when Im satisfied with the parameters.
```python
# Then augmenting
augmenter.run_augment()
```

