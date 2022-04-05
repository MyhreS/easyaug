# preprocess
The preprocess class contains functionality for changing images before it is feeded to the augmenter. Its only simple functions.
There needs to be specified input path and output path. And, there is no iteration down the subfolders. This is just extra functionality
if some preprocessing is needed.

## Resize
The class contains a function to resize images in a specified folder and output them at another specified folder.

Firstly you need to initialize the preprocess class.
```python
# Initialize the preprocess class.
from easyaug.preprocess import Preprocesser
preprocesser = Preprocesser()
```

Then you need to specify the input and output path. There is an option to specify what type of images it that will be resized in the parameters of the function. If you choose to specify type
it has to be either 'jpg' or 'png'. If you don't specify it, it will be automatically read all images.
```python
# Specify the input and output path.
preprocesser.specify_input_and_output_path('path/to/input/images', 'path/to/output/the/images', 'path/to/input/images')
```

Finally you can resize the images by doing this. In the parameter you choose a tuple that will be the new size of the images. It will output the resized images to the output path. 
```python
# Resize the images to (100, 100).
preprocesser.run_resize((100,100))
```

The complete code for this sequence:
```python
# Initialize the preprocess class.
from easyaug.preprocess import Preprocesser
preprocesser = Preprocesser()

# Specify the input and output path.
preprocesser.specify_input_and_output_path('path/to/input/images', 'path/to/output/the/images')

# Resize the images to (100, 100).
preprocesser.run_resize((100,100))
```