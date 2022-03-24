import glob
import os
import imageio


def read_all_images(path, type_of_image):
    # Getting all image names.
    image_names = read_all_imagenames(path, type_of_image)

    # Checking for errors on user input
    error_handling(image_names)

    # Getting all images by image names.
    images = []
    for image_name in image_names:
        images.append(read_a_image(image_name))
    return images


def read_every_x_image(path, x, type_of_image):
    # Getting all image names.
    image_names = read_all_imagenames(path, type_of_image)

    # Checking for errors on user input
    error_handling(image_names, x)

    # Getting every x image
    images = []
    for index in range(0, len(image_names), x):
        images.append(read_a_image(image_names[index]))
    return images


def read_first_x_images(path, x, type_of_image):
    # Getting all image names.
    image_names = read_all_imagenames(path, type_of_image)

    # Checking for errors on user input
    error_handling(image_names, x)

    # If first x is larger than the amount of images it will be set to the amount of images.
    if x > len(image_names):
        x = len(image_names)

    # Getting first x images.
    images = []
    for index in range(0, x):
        images.append(read_a_image(image_names[index]))
    return images


def read_last_x_images(path, x, type_of_image):
    # Getting all image names.
    image_names = read_all_imagenames(path, type_of_image)

    # Checking for errors on user input
    error_handling(image_names, x)

    # If first x is larger than the amount of images it will be set to the amount of images.
    if x > len(image_names):
        x = len(image_names)

    # Getting last x images.
    images = []
    for index in range(len(image_names)-x, len(image_names)):
        images.append(read_a_image(image_names[index]))
    return images


def read_x_images(path, x, type_of_image):
    # Getting all image names.
    image_names = read_all_imagenames(path, type_of_image)

    # Checking for errors on user input
    error_handling(image_names, x)

    # If first x is larger than the amount of images it will be set to the amount of images.
    if x > len(image_names):
        x = len(image_names)

    images = []
    if x > 1:
        # Finding how much to step for each iteration to read x images.
        step = int((len(image_names)+x)/x)

        # Getting 10 images with equal space inbetween.
        for index in range(0, len(image_names), step):
            images.append(read_a_image(image_names[index]))
    else:
        index = int(len(image_names)/2)
        images.append(read_a_image(image_names[index]))

    return images


def read_a_image(image_path):
    return imageio.imread(image_path)


def read_all_imagenames(path, type_of_image):
    # If path is not set with / it will add it.
    if path[-1] != "/":
        path = path+"/"

    # Find the images in this folder.
    image_names = []
    if type_of_image is None:
        image_names = glob.glob(path + "*")
    elif type_of_image == "jpg" or type_of_image == "png":
        image_names = glob.glob(path + "*."+type_of_image)

    # If it finds a folder it will go into that and get those images too. Recursive.
    is_directories = []
    for image_name in image_names:
        if os.path.isdir(image_name):
            is_directories.append(image_name)
            image_names += read_all_imagenames(image_name, type_of_image)

    # Removes the directory paths.
    for is_directory in is_directories:
        image_names.remove(is_directory)

    return image_names


def error_handling(image_names, x=None):
    if x is not None:
        if x < 1:
            raise ValueError("X must be larger than 0.")

    if len(image_names) == 0:
        raise Exception("There was not found any images.")