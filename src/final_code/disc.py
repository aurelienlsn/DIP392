from color import Color

class Disc:
    def __init__(self, color):
        if color is None:
            raise ValueError("Disc color cannot be None")
        self.discColor = color
