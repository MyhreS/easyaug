"""
This module is used to augment images.
"""

from image_worker.augment import run_view
from image_worker.augment import augmenting_types
from imgaug import augmenters as iaa

class Augmenter:
    """
    A class used to augment images. When creating an instance of this class, you can specify the path to your data. Then
    you can specify the augmenting types. These will be set to a todolist. So when finally you choose to either view a few augmented images or augment all images and save them
    to a new directory the todolist will be executed for each image.
    """
    def __init__(self):
        self.path = None
        self.type_of_image = None
        self.augmentation_todo = iaa.Sequential() # For each image in the specified path, do the augmenting added to the ttodo list.
        self.todo_names = [] # Names of each of the augmentation_todo.

        print("Augmenter initialized")

    def specify_path(self, path, type_of_image=None):
        """
        Specify the path to the data.

        Parameters
        ----------
        path : str
            The path to the data.
        type_of_image : str
            The type of the image.

        Raises
        ------
        ValueError
            If the path is not a string.
            If type_of_image is not None, "jpg" og "png".

        Returns
        -------

        Examples
        --------
        >>> augmenter.specify_path("/home/user/data/", "jpg")
        Specified path to data: /home/user/data/ and type of image: jpg
        """

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

    # Functions that makes image clearer or blurrier.
    def do_gaussianBlur(self, intensity_from=0.5, intensity_to=3.0):
        """
        Blur the image with a gaussian blur. It augments with a random intensity between the specified parameters.

        Parameters
        ----------
        intensity_from : float
            The lowest intensity of the gaussian blur. Ranging from 0 to unlimited. Intensity 0 is no blur. Intensity 3.0 is much blur.
        intensity_to : float
            The highest intensity of the gaussian blur. Ranging from 0 to unlimited.  Intensity 0 is no blur. Intensity 3.0 is much blur.

        Raises
        ------
        ValueError
            If the intensity_from or intensity_to is not a float or int.
            If the intensity_from is greater than the intensity_to.
            If the intensity_from or intensity_to is less than 0.0.

        Returns
        -------

        Examples
        --------
        >>> from image_worker.augment import Augmenter
        >>> augmenter = Augmenter()
        >>> augmenter.do_gaussianBlur(0.5, 3.0)
        Added gaussian blur to the augmenting todo list.

        """
        augmenting = augmenting_types.gaussianBlur(intensity_from, intensity_to)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Gaussian Blur")

    def do_sharpen(self, intensity_from=0.1, intensity_to=0.5):
        """
        Sharpen the image with a sharpen. It augments with a random intensity between the specified parameters.

        Parameters
        ----------
        intensity_from : float
            The lowest percent intensity of the sharpen. Ranging from 0.0 (0%) to 1.0 (100%). Intensity 0 is no sharpen. Intensity 0.7 is much sharpen.
        intensity_to : float
            The highest percent intensity of the sharpen. Ranging from 0.0 (0%) to 1.0 (100%). Intensity 0 is no sharpen. Intensity 0.7 is much sharpen.

        Raises
        ------
        ValueError
            If the intensity_from or intensity_to is not a float or int.
            If the intensity_from is greater than the intensity_to.
            If the intensity_from or intensity_to less than 0.0.
            If the intensity_from or intensity_to is greater than 1.0.

        Returns
        -------

        Examples
        --------
        >>> from image_worker.augment import Augmenter
        >>> augmenter = Augmenter()
        >>> augmenter.do_sharpen(0.1, 0.5)
        Added sharpen to the augmenting todo list.
        """
        augmenting = augmenting_types.sharpen(intensity_from, intensity_to)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Sharpen")

    def do_saltAndPepper(self, intensity=0.1):
        """
        
        """
        augmenting = augmenting_types.saltAndPepper(intensity)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Salt and Pepper")

    def do_additiveGuassianNoise(self, intensity_from=5, intensity_to=50):
        augmenting = augmenting_types.additiveGuassianNoise(intensity_from, intensity_to)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Additive Guassian Noise")

    # Functions that changes the position of the image.
    def do_rotate(self, rotation_left=180, rotation_right=180):
        augmenting = augmenting_types.rotation(rotation_left, rotation_right)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Rotation")

    def do_pad(self, left=20, right=20, top=20, bottom=20):
        augmenting = augmenting_types.pad(left, right, top, bottom)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Pad")

    def do_scale(self, zoom_out=0.5, zoom_in=1.5):
        augmenting = augmenting_types.scale(zoom_out, zoom_in)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Scale")


    # Combined functions
    def do_guassianBlur_and_rotate(self, guassianBlur_intensity_from=0.5, guassianBlur_intensity_to=3.0, rotate_rotation_left=180, rotate_rotation_right=180):
        augmenting = augmenting_types.guassianBlur_and_rotate(guassianBlur_intensity_from, guassianBlur_intensity_to, rotate_rotation_left, rotate_rotation_right)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Gaussian Blur and Rotation")

    def to_guassianBlur_and_pad(self, guassianBlur_intensity_from=0.5, guassianBlur_intensity_to=3.0, pad_left=20, pad_right=20, pad_top=20, pad_bottom=20):
        augmenting = augmenting_types.guassianBlur_and_pad(guassianBlur_intensity_from, guassianBlur_intensity_to, pad_left, pad_right, pad_top, pad_bottom)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Gaussian Blur and Pad")

    def do_guassianBlur_and_scale(self, guassianBlur_intensity_from=0.5, guassianBlur_intensity_to=3.0, scale_zoom_out=0.5, scale_zoom_in=1.5):
        augmenting = augmenting_types.guassianBlur_and_scale(guassianBlur_intensity_from, guassianBlur_intensity_to, scale_zoom_out, scale_zoom_in)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Gaussian Blur and Scale")

    def do_rotate_and_scale(self, rotate_rotation_left=180, rotate_rotation_right=180, scale_zoom_out=0.5, scale_zoom_in=1.5):
        augmenting = augmenting_types.rotate_and_scale(rotate_rotation_left, rotate_rotation_right, scale_zoom_out, scale_zoom_in)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Rotation and Scale")

    def do_sharpen_and_rotate(self, sharpen_intensity_from=0.1, sharpen_intensity_to=0.5, rotate_rotation_left=180, rotate_rotation_right=180):
        augmenting = augmenting_types.sharpen_and_rotate(sharpen_intensity_from, sharpen_intensity_to, rotate_rotation_left, rotate_rotation_right)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Sharpen and Rotation")

    def do_sharpen_and_pad(self, sharpen_intensity_from=0.1, sharpen_intensity_to=0.5, pad_left=20, pad_right=20, pad_top=20, pad_bottom=20):
        augmenting = augmenting_types.sharpen_and_pad(sharpen_intensity_from, sharpen_intensity_to, pad_left, pad_right, pad_top, pad_bottom)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Sharpen and Pad")

    def do_sharpen_and_scale(self, sharpen_intensity_from=0.1, sharpen_intensity_to=0.5, scale_zoom_out=0.5, scale_zoom_in=1.5):
        augmenting = augmenting_types.sharpen_and_scale(sharpen_intensity_from, sharpen_intensity_to, scale_zoom_out, scale_zoom_in)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Sharpen and Scale")

    def do_saltAndPepper_and_rotate(self, saltAndPepper_intensity=0.1, rotate_rotation_left=180, rotate_rotation_right=180):
        augmenting = augmenting_types.saltAndPepper_and_rotate(saltAndPepper_intensity, rotate_rotation_left, rotate_rotation_right)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Salt and Pepper and Rotation")

    def do_saltAndPepper_and_pad(self, saltAndPepper_intensity=0.1, pad_left=20, pad_right=20, pad_top=20, pad_bottom=20):
        augmenting = augmenting_types.saltAndPepper_and_pad(saltAndPepper_intensity, pad_left, pad_right, pad_top, pad_bottom)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Salt and Pepper and Pad")

    def do_saltAndPepper_and_scale(self, saltAndPepper_intensity=0.1, scale_zoom_out=0.5, scale_zoom_in=1.5):
        augmenting = augmenting_types.saltAndPepper_and_scale(saltAndPepper_intensity, scale_zoom_out, scale_zoom_in)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Salt and Pepper and Scale")

    def do_additiveGuassianNoise_and_rotate(self, additiveGuassianNoise_intensity_from=5, additiveGuassianNoise_intensity_to=50, rotate_rotation_left=180, rotate_rotation_right=180):
        augmenting = augmenting_types.additiveGuassianNoise_and_rotate(additiveGuassianNoise_intensity_from, additiveGuassianNoise_intensity_to, rotate_rotation_left, rotate_rotation_right)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Additive Guassian Noise and Rotation")

    def do_additiveGuassianNoise_and_pad(self, additiveGuassianNoise_intensity_from=5, additiveGuassianNoise_intensity_to=50, pad_left=20, pad_right=20, pad_top=20, pad_bottom=20):
        augmenting = augmenting_types.additiveGuassianNoise_and_pad(additiveGuassianNoise_intensity_from, additiveGuassianNoise_intensity_to, pad_left, pad_right, pad_top, pad_bottom)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Additive Guassian Noise and Pad")

    def do_additiveGuassianNoise_and_scale(self, additiveGuassianNoise_intensity_from=5, additiveGuassianNoise_intensity_to=50, scale_zoom_out=0.5, scale_zoom_in=1.5):
        augmenting = augmenting_types.additiveGuassianNoise_and_scale(additiveGuassianNoise_intensity_from, additiveGuassianNoise_intensity_to, scale_zoom_out, scale_zoom_in)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Additive Guassian Noise and Scale")


    # Testing the augmenation by visualising the images.
    def run_view(self):
        # Raises ValueError if something is wrong.
        if self.path is None:
            raise ValueError("No path specified")
        elif len(self.augmentation_todo) == 0:
            raise ValueError("No augmentation specified")
        else:
            run_view.view_augment(self.path, self.type_of_image, self.augmentation_todo, self.todo_names)

    def stats(self):
        pass

    # Augmenting the images.
    def run_augment(self, images=None):
        # Runs the augmentation on the images
        # Reads one image from the specified path at the time and runs the augmentation on it. Then writes the augmented image to disk in a folder called originalImagesFoldersName_augmented.
        pass

