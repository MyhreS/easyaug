import glob
import os
from datetime import datetime
from random import random

import imageio
from matplotlib import pyplot as plt


def view_augment(images_path, type_of_image, todo):
    # Reads all the images in the folder.
    imagenames = read_all_imagenames(images_path, type_of_image)

    # If imagename is empty raise an error.
    if len(imagenames) == 0:
        raise Exception("No images found in the specified path.")


    # Pick 9 random items from imagenames. Cannot be the same.
    random_images = []
    if len(imagenames) > 9:
        while len(random_images) < 9:
            random_image = imagenames[int(len(imagenames)*random())]
            if random_image not in random_images:
                random_images.append(random_image)
    else:
        random_images = imagenames

    # Read the images.
    images = []
    for random_image in random_images:
        images.append(read_a_image(random_image))

    # Clear previous plots in SciView.
    plt.close("all")

    # Create an empty figure in pyplot.
    fig = plt.figure(figsize=(10, 10))
    # A string with time and date.
    fig.suptitle("A spacer between new and old Plots in SciView", fontsize=25)
    fig.show()
    # Plot the original images.
    pyplot_9_images(images)



def read_all_imagenames(path, type_of_image):
    # If path is not set with / it will add it.
    if path[-1] != "/":
        path = path+"/"

    # Find the images in this folder.
    imagenames = []
    if type_of_image is None:
        imagenames = glob.glob(path + "*")
    elif type_of_image == "jpg" or type_of_image == "png":
        imagenames = glob.glob(path + "*."+type_of_image)

    # If it finds a folder it will go into that and get those images too. Recursive.
    is_directories = []
    for image_name in imagenames:
        if os.path.isdir(image_name):
            is_directories.append(image_name)
            imagenames += read_all_imagenames(image_name, type_of_image)

    # Removes the directory paths.
    for is_directory in is_directories:
        imagenames.remove(is_directory)
    return imagenames

def read_a_image(image_path):
    image = imageio.imread(image_path)
    image._name = image_path
    return image

# Creating a pyplot containing at maximum 9 images.
def pyplot_9_images(images_max_9):
    # Predefined values.
    columns = 3 # If columns or rows is changed more code needs to be changes.
    rows = 3
    height_of_pyplot = 10
    width_of_pyplot = 10

    # Plotting.
    fig = plt.figure(figsize=(width_of_pyplot, height_of_pyplot))
    for i in range(0, len(images_max_9)):
        # Preparing plot for image.
        fig.add_subplot(rows, columns, i + 1)
        # Plotting image in preparet plot.
        plt.imshow(images_max_9[i])
        plt.axis("off")
        plt.title(get_name(images_max_9[i]._name))
    fig.tight_layout()
    plt.show()

def get_name(image_path):
    image_path_split = image_path.split("\\")
    imagename_dot_something = image_path_split[-1].split(".")
    imagename = imagename_dot_something[0]
    return imagename