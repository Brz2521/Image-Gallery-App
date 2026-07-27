class Gallery:

    def __init__(self):
        self.images = []

    def post_image(self, image):
        self.images.append(image)

    def delete_image(self, image):
        image.delete()
        self.images.remove(image)

    def duplicate_image(self, image):
        duplicate = image.duplicate()
        self.images.append(duplicate)

    def get_images(self):
        return self.images