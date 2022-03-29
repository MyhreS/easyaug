from image_worker.augment import run_view
from image_worker.augment import augmenting_types
from imgaug import augmenters as iaa

class Augmenter:
    def __init__(self):
        self.path = None
        self.type_of_image = None
        self.todo = iaa.Sequential() # For each image in the specified path, do the augmenting added to the ttodo list.

        print("Augmenter initialized")

    def specify_path(self, path, type_of_image=None):

        if type_of_image is not None:
            if type_of_image != "jpg" or type_of_image != "png":
                raise ValueError("Type of image must be None, jpg or png")
        if path is None:
            raise ValueError("No path specified")
        elif type(path) is not str:
            raise ValueError("Path must be a string")
        else:
            self.path = path
            self.type_of_image = type_of_image
            print("Path specified")

    def do_gaussianBlur(self, guassian_intensity_from, guassian_intensity_to):
        augmenting = augmenting_types.gaussianBlur(guassian_intensity_from, guassian_intensity_to)
        self.todo.add(augmenting)

    def run_view(self):
        # Raises ValueError if something is wrong.
        if self.path is None:
            raise ValueError("No path specified")
        elif len(self.todo) == 0:
            raise ValueError("No augmentation specified")
        else:
            run_view.view_augment(self.path, self.type_of_image, self.todo)

        # Run the view

        # Shows a plot of 9 images with their respective augmented versions
        # For example shows 9 images a plot with guassian blur and 9 images in a plot with rotation
        # The header for the plot is the name type of augmentation.
        # Does not write the augmented images to disk. Just shows the images.

    def run_augment(self, images=None):
        # Runs the augmentation on the images
        # Reads one image from the specified path at the time and runs the augmentation on it. Then writes the augmented image to disk in a folder called originalImagesFoldersName_augmented.
        pass

