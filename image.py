

class Image:
    """Creates the picture objects"""
    def __init__(self, img_arr):
        self.image = img_arr

    def get_image(self):
        """Returns an whole image"""
        return self.image

    def get_row(self, row):
        """Returns a whole row"""
        return self.image[row]

    def get_col(self, row, col):
        """Returns a single column"""
        return self.image[row][col]