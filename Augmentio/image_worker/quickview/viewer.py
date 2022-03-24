from image_worker.quickview import read

class Viewer:
    def __init__(self):
        self.images = []
        self.image_names = []
        print("Quickview initialized")

    def read_all_images(self, path, type_of_image=None):
        self.images = read.read_all_images(path, type_of_image)
        return self.images


    def read_every_x_image(self, path, x, type_of_image=None):
        self.images = read.read_every_x_image(path, x, type_of_image)
        return self.images

    def read_first_x_images(self, path, x, type_of_image=None):
        self.images = read.read_first_x_images(path, x, type_of_image)
        return self.images

    def read_last_x_images(self, path, x, type_of_image=None):
        self.images = read.read_last_x_images(path, x, type_of_image)
        return self.images

    def read_x_images(self, path, x, type_of_image=None):
        self.images = read.read_x_images(path, x, type_of_image)
        return self.images

    def read_a_image(self, path):
        self.images.append(read.read_a_image(path))
        return self.images

    def read_all_imagenames(self, path, type_of_image=None):
        self.image_names = read.read_all_imagenames(path, type_of_image)
        read.error_handling(self.image_names)
        return self.image_names

    def read_every_x_imagename(self, path, x, type_of_image=None):
        print(path)
        # Return image_names

    def read_first_x_imagenames(self, path, x, type_of_image=None):
        print(path)
        # Return image_names

    def read_last_x_imagenames(self, path, x, type_of_image=None):
        print(path)
        # Return image_names

    def view_images(self, images=None):
        print("Images:")
        # Show images

    def view_image_names(self, image_names=None):
        print("Image names:")
        # Show image_names





