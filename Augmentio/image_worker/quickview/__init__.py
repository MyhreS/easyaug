class Quickviewer:
    def __init__(self):
        self.images = []
        self.image_names = []
        print("Quickview initialized")

    def read_files(self, path, type_of_file=None):
        print(path)
