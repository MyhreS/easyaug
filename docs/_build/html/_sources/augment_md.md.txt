# augment
The main purpose of the easyaug framework is augmenting images. This package contains pre-defined augmentations that is a part of the Augmenter class.
It's simple with really only 3 steps to it. Firstly specify the input path for the images. Secondly specify the types of augmentation done on each image. 
Lastly run the augmenter or do a test view before you do it.

## Augmenting images
To get access to the functionallity you need to initialize the Augmenter class.
```python
# Initialize the augmenter.
from easyaug.augment import Augmenter
augmenter = Augmenter()
```

Now you need to specify the path the input images. There is an option to specify what type of images that are going to be read. If specified this can only be as 'jpg' or 'png'.
```python
# Specify the path to the images.
augmenter.specify_input_path('/path/to/images')
```
Where you specify the path to depends on how many of your images you want to change. If specified in this case to the 'images' folder. The augmenter will
follow the directory downwards the subdirectories and find all the images. In this case both the images in the 'panda' folder and the 'tiger' folder:

```
# Example directory:
├── images
│   ├── panda
│   │   ├── panda_0.jpg
│   │   └── panda_1.jpg
│   ├── tiger
│   │   ├── tiger_0.jpg
│   │   └── tiger_1.jpg
```
It is also possible to specify an output path, but this is not necessary. The augmented images will by default be placed in similar folder next to the specified input path (folder).


Anyways, after specifying the path  you can add different augmenting types to a todo list. How it works is for each augmenting type in the todo list it will augment every image by them.
Told differently. Lets say you add 'sharpen' and 'gaussian blur' to the todo list. Each image that is in the specified input path will be augmented by both of them.

You specify them augmentation types like this. In this case 'sharpen' and 'gaussian blur' :
```python
# Adding two types of augmentationto the todo list.
augmenter.do_sharpen()
augmenter.do_gaussianBlur()
```
When running they will produce these images out of 1 image:
```
# Before augmentation:
panda_1.jpg

# After augmentation:
panda_1.jpg
panda_1_sharpen.jpg
panda_1_gaussianBlur.jpg
```
These augmentation types have default parameters, but can easily be changed to your liking.
But, there will be no augmentation before you run the 'run_augmenter' function.
```python
# Run the augmentation with the specified augmentation types.
augmenter.run_augmenter()
```
After running the function above with the specified augmentaion types added to the todo list, the result would be this:
```
# Example directory: Original images in their folders
├── images
│   ├── panda
│   │   ├── panda_0.jpg
│   │   └── panda_1.jpg
│   ├── tiger
│   │   ├── tiger_0.jpg
│   │   └── tiger_1.jpg
│ 

# Example directory: New folders with their augmented images (including the original images).
# Created by the augmenter.
├── images_augmented
│   ├── panda_augmented
│   │   ├── panda_0.jpg
│   │   ├── panda_0_sharpen.jpg
│   │   ├── panda_0_gaussianBlur.jpg
│   │   ├── panda_1.jpg
│   │   ├── panda_1_sharpen.jpg
│   │   └── panda_1_gaussianBlur.jpg
│   ├── tiger_augmented
│   │   ├── tiger_0.jpg
│   │   ├── tiger_0_sharpen.jpg
│   │   ├── tiger_0_gaussianBlur.jpg
│   │   ├── tiger_1.jpg
│   │   ├── tiger_1_sharpen.jpg
│   │   └── tiger_1_gaussianBlur.jpg
```
As shown there will be autmatically created folders for the augmented images (that also include the original images). If an output path
is specified, the root folder will not be created, but the subfolders will.

But, lets say you are not sure if you know how the augmentated images will look. Then instead of calling hte 'run_augmenter' function you can call the 'run_view' function.

```python
# Run a test view of the augmentation to visualize the result before augmenting.
augmenter.run_view()
```
This will take at maximum 9 random images from the specified input path and show them in multiple pyplots. In this case first a pyplot of 9 original images.
Then a pyplot of the 9 original images augmented by the 'sharpen' augmentation type. Then a pyplot of the 9 original images augmented by the 'gaussian blur' 
augmentation type. This is so you can tweek the parameters of the augmentation types added to the todo list before actually running the 'run_augment' function which
writes the images to folders.

The complete code for this sequence:
```python
# Initialize the augmenter.
from easyaug.augment import Augmenter
augmenter = Augmenter()

# Specify the path to the images.
augmenter.specify_input_path('/path/to/images')

# Adding two types of augmentationto the todo list.
augmenter.do_sharpen()
augmenter.do_gaussianBlur()

# Run a test view of the augmentation to visualize the result before augmenting.
augmenter.run_view() # Comment this when done testing.

# Run the augmentation with the specified augmentation types.
#augmenter.run_augment() # Remove comment when done testing.
```




