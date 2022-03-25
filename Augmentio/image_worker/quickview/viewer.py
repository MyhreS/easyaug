from image_worker.quickview import read
from image_worker.quickview import view

class Viewer:
    def __init__(self):
        self.images = []
        self.imagenames = []
        print("Quickview initialized")

    def read_all_images(self, path, type_of_image=None):
        self.images = read.read_all_images(path, type_of_image)
        read.no_images_error_handling(len(self.images))
        print("Read", len(self.images), "images.")
        return self.images

    def read_every_x_image(self, path, x, type_of_image=None):
        self.images = read.read_every_x_image(path, x, type_of_image)
        read.no_images_error_handling(len(self.images))
        print("Read", len(self.images), "images.")
        return self.images

    def read_first_x_images(self, path, x, type_of_image=None):
        self.images = read.read_first_x_images(path, x, type_of_image)
        read.no_images_error_handling(len(self.images))
        print("Read", len(self.images), "images.")
        return self.images

    def read_last_x_images(self, path, x, type_of_image=None):
        self.images = read.read_last_x_images(path, x, type_of_image)
        read.no_images_error_handling(len(self.images))
        print("Read", len(self.images), "images.")
        return self.images

    # Fails at read 50 images of in total 64 images
    # Fails at read 20 images of in total 64 images
    """
    def read_x_images(self, path, x, type_of_image=None):
        self.images = read.read_x_images(path, x, type_of_image)
        read.no_images_error_handling(len(self.images))
        return self.images
    """

    def read_a_image(self, path):
        self.images.append(read.read_a_image(path))
        read.no_images_error_handling(len(self.images))
        print("Read 1 image.")
        return self.images

    def read_all_imagenames(self, path, type_of_image=None):
        self.imagenames = read.read_all_imagenames(path, type_of_image)
        read.no_images_error_handling(len(self.imagenames))
        print("Read", len(self.imagenames), "imagenames.")
        return self.imagenames


    def read_every_x_imagename(self, path, x, type_of_image=None):
        self.imagenames = read.read_every_x_imagename(path, x, type_of_image)
        read.no_images_error_handling(len(self.imagenames))
        print("Read", len(self.imagenames), "imagenames.")
        return self.imagenames


    def read_first_x_imagenames(self, path, x, type_of_image=None):
        self.imagenames = read.read_first_x_imagenames(path, x, type_of_image)
        read.no_images_error_handling(len(self.imagenames))
        print("Read", len(self.imagenames), "imagenames.")
        return self.imagenames

    def read_last_x_imagenames(self, path, x, type_of_image=None):
        self.imagenames = read.read_last_x_imagenames(path, x, type_of_image)
        read.no_images_error_handling(len(self.imagenames))
        print("Read", len(self.imagenames), "imagenames.")
        return self.imagenames


    def view_images(self, maximum=9, images=None):
        if images is not None:
            read.no_images_error_handling(len(images))
            view.view_images(images, maximum)
        elif len(self.images) != 0:
            view.view_images(self.images, maximum)
        else:
            raise ValueError("No images found.")

    def view_imagenames(self, maximum=20, imagenames=None):
        if imagenames is not None:
            read.no_images_error_handling(len(imagenames))
            view.view_imagesnames(imagenames, maximum)
        elif len(self.imagenames) != 0:
            view.view_imagesnames(self.imagenames, maximum)
        elif len(self.images) != 0:
            view.view_imagesnames_from_images(self.images, maximum)
        else:
            raise ValueError("No imagenames or images found.")






