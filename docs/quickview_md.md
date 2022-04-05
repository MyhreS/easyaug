# quickview
The quickview consists of primary two parts. The first is viewing images and the second is viewing image names. They both have the same structure.

## Reading and viewing images
The first primary part is reading and viewing images. This is done by using one of the 'read_images' functions together with the view image function. Here is how:

Firstly we need to initialize the quickview class to use its functionality.

```python
# Initialize the quickviewer class.
from easyaug.quickview import Quickviewer
quickviewer = Quickviewer()
```
Now that we have initialized it we have access to its functions. You have now the possiblity read the images in different ways. 
You can choose between reading all, the first x or many more ways of reading the images. In the code bellow we choose to read the first 2 images.

```python
# Read the first 2 images.
quickviewer.read_first_x_images("path/to/images", 2)
```
As you can see we specified the first 2 images shall be read. But also we specified the path to the images. It will find all the images in the folder and even iterate down the subfolders to find more.
So lets say you specified the path to the 'train' dataset it will find all the images in panda, cat and dog folders. But, since you specified the first 2 images, it will only read the first 2 images in the panda folder.

```
├── data
│   ├── train
│   │   ├── panda
│   │   │   ├── panda_1.jpg
│   │   │   └── panda_2.jpg
│   │   ├── cat.jpg
│   │   └── dog.jpg
```

What images you want displayed depends on how you read the data. When you are done reading the data you can display them using this function.

```python
# Display the images.
quickviewer.view_images()
```
This will display by default maximum 9 images in a pyplot window. You can change the maximum in the parameters of the function if you want.
Or you could even pass in your own list of images to it. 

The complete code of this sequence.

```python
# Initialize the quickviewer class.
from easyaug.quickview import Quickviewer
quickviewer = Quickviewer()

# Read the first 2 images.
quickviewer.read_first_x_images("path/to/images", 2)

# Display the images.
quickviewer.view_images()
```
NOTE: If you chose to use multiple read images functions of the class it will not append the images, instead it will overwrite old with the new.

## Reading and viewing image names
The second part of the quickview is viewing the image names. This is done by using one of the 'read_imagenames' functions and the view imagenames function. Here is how:

Firstly we need to initialize the quickview class to use its functionality.

```python
# Initialize the quickview class.
from easyaug.quickview import Quickviewer
quickviewer = Quickviewer()
```

Now that we have initialized it we have access to its functions. You have now the possiblity read the image names in different ways. 
You can choose between reading all, the first x or many more ways of reading the image names. In the code bellow we choose to read the first 2 image names.

```python
# Read the names of the first 2 images.
quickviewer.read_first_x_imagenames("path/to/images", 2)
```
As you can see we specified the first 2 image names of the images in the path shall be read. But also we specified the path to the images. It will find all the images in the folder and even iterate down the subfolders to find more.
So lets say you specified the path to the 'train' dataset it will find all the images in panda, cat and dog folders. But, since you specified the first 2 imagenames, it will only read the name of the first 2 images.

```
├── data
│   ├── train
│   │   ├── panda
│   │   │   ├── panda_1.jpg
│   │   │   ├── panda_2.jpg
│   │   ├── cat.jpg
│   │   └── dog.jpg
```

What image names you want displayed depends on how you read the data. When you are done reading the data you can display them using this function.

```python
# Display the image names.
quickviewer.view_imagenames()
```
This will print to terminal by default maximum 20 image names. You can change the maximum in the parameters of the function if you want.
Or you could even pass in your own list of image names to it. 

The complete code of this sequence.

```python
# Initialize the quickview class.
from easyaug.quickview import Quickviewer
quickviewer = Quickviewer()

# Read the names of the first 2 images.
quickviewer.read_first_x_imagenames("path/to/images", 2)

# Print the image names.
quickviewer.view_imagenames()
```
NOTE: If you chose to use multiple read images functions of the class it will not append the images, instead it will overwrite old with the new.
