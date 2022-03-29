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
    def do_gaussianBlur(self, guassian_intensity_from, guassian_intensity_to):
        augmenting = augmenting_types.gaussianBlur(guassian_intensity_from, guassian_intensity_to)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Gaussian Blur")

    def do_sharpen(self, intensity_from, intensity_to):
        augmenting = augmenting_types.sharpen(intensity_from, intensity_to)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Sharpen")

    # Functions that changes the position of the image.
    def do_rotation(self, rotation_from, rotation_to):
        augmenting = augmenting_types.rotation(rotation_from, rotation_to)
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
    def do_guassianBlur_and_rotation(self, guassian_intensity_from, guassian_intensity_to, rotation_from, rotation_to):
        augmenting = augmenting_types.guassianBlur_and_rotation(guassian_intensity_from, guassian_intensity_to, rotation_from, rotation_to)
        self.augmentation_todo.add(augmenting)
        self.todo_names.append("Gaussian Blur and Rotation")



    def run_view(self):
        # Raises ValueError if something is wrong.
        if self.path is None:
            raise ValueError("No path specified")
        elif len(self.augmentation_todo) == 0:
            raise ValueError("No augmentation specified")
        else:
            run_view.view_augment(self.path, self.type_of_image, self.augmentation_todo, self.todo_names)


    def run_augment(self, images=None):
        # Runs the augmentation on the images
        # Reads one image from the specified path at the time and runs the augmentation on it. Then writes the augmented image to disk in a folder called originalImagesFoldersName_augmented.
        pass

