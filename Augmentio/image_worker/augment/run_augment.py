import glob
import os


class Folder:
    def __init__(self, folder_path, name_of_folder):
        self.folder_path = folder_path
        self.name_of_folder = name_of_folder
        self.list_of_folders = []
        self.list_of_images = []





def augment(path, output_path, type_of_image, augmentation_todo, todo_names):
    # If path does not end with a slash, add one.
    path = fix_folder_path(path)

    # Create a list of folders
    first_folder = Folder(path, name_of_folder(path))

    # Iterates through the first folder to find all images and folders
    iterate_folder(first_folder, type_of_image)

    # Iterates through first_folder to print all folders and images
    print_folder(first_folder)

def fix_folder_path(path):
    """Fix the path so that it ends with a slash."""
    if path[-1] != '/':
        path += '/'
    return path

def name_of_folder(path):
    """Return the name of the folder in the path."""
    return path.split('/')[-2]

def iterate_folder(folder, type_of_image):

    # Using glob finds all paths in the folder.folder_path
    for path in glob.glob(folder.folder_path + '*'):
        path = fix_slashes(path)
        # If a path is a folder, create a new folder object and add it to the list of folders.
        if os.path.isdir(path):
            path = fix_folder_path(path)
            new_folder = Folder(path, name_of_folder(path))
            folder.list_of_folders.append(new_folder)
            iterate_folder(new_folder, type_of_image)
        # If a path is an image and the type of image is not specified, add it to the list of images.
        elif os.path.isfile(path) and type_of_image is None:
            folder.list_of_images.append(path)
        # If a path is an image and the type of image is specified, add it to the list of images if it matches the type of image.
        elif os.path.isfile(path) and type_of_image is not None:
            if type_of_image == find_type_of_image(path):
                folder.list_of_images.append(path)


def find_type_of_image(path):
    """Return the type of image in the path."""
    return path.split('.')[-1]

def print_folder(first_folder):
    """Print the folders and images in the folder."""
    print('Folder: ' + first_folder.name_of_folder)
    for folder in first_folder.list_of_folders:
        print_folder(folder)
    for image in first_folder.list_of_images:
        print(image)

def fix_slashes(path):
    """Fix the slashes in the path."""
    path = path.replace('\\', '/')
    return path







