class Augmenter:

    def __init__(self):
        self.image_path = None
        self.todo = [] # For each image in the specified path, do the augmenting added to the ttodo list.
        print("Augmenter initialized")

    def specify_path(self, image_path):
        self.image_path = image_path

    def do_gaussuan_blur(self, guassian_intensity):
        # Do gaussian blur
        pass

    def do_rotate(self, image):
        # Rotate image
        pass

    def run_test_augment_and_view(self, images=None):
        # Shows a plot of 9 images with their respective augmented versions
        # For example shows 9 images a plot with guassian blur and 9 images in a plot with rotation
        # The header for the plot is the name type of augmentation.
        # Does not write the augmented images to disk. Just shows the images.
        return images

    def run_augment(self, images=None):
        # Runs the augmentation on the images
        # Reads one image from the specified path at the time and runs the augmentation on it. Then writes the augmented image to disk in a folder called originalImagesFoldersName_augmented.

        return images

