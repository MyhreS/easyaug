from image_worker.augment import run_view
from image_worker.augment import augmenting_types
from imgaug import augmenters as iaa

class Augmenter:
    def __init__(self):
        self.path = None
        self.type_of_image = None
        self.augmentation_todo = iaa.Sequential() # For each image in the specified path, do the augmenting added to the ttodo list.
        self.todo_names = [] # Names of each of the augmentation_todo.

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

    # Functions that makes image clearer or blurrier.
    def do_gaussianBlur(self, intensity_from=0.5, intensity_to=3.0):
        augmenting = augmenting_types.gaussianBlur(intensity_from, intensity_to)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Gaussian Blur")

    def do_sharpen(self, intensity_from=0.1, intensity_to=0.5):
        augmenting = augmenting_types.sharpen(intensity_from, intensity_to)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Sharpen")

    def do_saltAndPepper(self, intensity=0.1):
        augmenting = augmenting_types.saltAndPepper(intensity)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Salt-n-Pepper")

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

    def do_guassianBlur_and_scale(self, guassianBlur_intensity_from=0.5, guassianBlur_intensity_to=3.0, scale_zoom_out=0.5, scale_zoom_in=1.5):
        augmenting = augmenting_types.guassianBlur_and_scale(guassianBlur_intensity_from, guassianBlur_intensity_to, scale_zoom_out, scale_zoom_in)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Gaussian Blur and Scale")

    def do_rotate_and_scale(self, rotate_rotation_left=180, rotate_rotation_right=180, scale_zoom_out=0.5, scale_zoom_in=1.5):
        augmenting = augmenting_types.rotate_and_scale(rotate_rotation_left, rotate_rotation_right, scale_zoom_out, scale_zoom_in)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Rotation and Scale")

    



    # Testing the augmenation by visualising the images.
    def run_view(self):
        # Raises ValueError if something is wrong.
        if self.path is None:
            raise ValueError("No path specified")
        elif len(self.augmentation_todo) == 0:
            raise ValueError("No augmentation specified")
        else:
            run_view.view_augment(self.path, self.type_of_image, self.augmentation_todo, self.todo_names)

    # Augmenting the images.
    def run_augment(self, images=None):
        # Runs the augmentation on the images
        # Reads one image from the specified path at the time and runs the augmentation on it. Then writes the augmented image to disk in a folder called originalImagesFoldersName_augmented.
        pass

