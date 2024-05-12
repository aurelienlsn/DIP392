class Color:
    def __init__(self, red, green, blue):
        if (red, green, blue) not in [(255, 0, 0), (255, 255, 0)]:
            raise ValueError("Invalid color: Only red and yellow colors are allowed.")
        
        self.red = red
        self.green = green
        self.blue = blue
