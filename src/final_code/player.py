from disc import Disc

class Player:
    def __init__(self, name, color):
        if color not in ['red', 'yellow']:
            raise ValueError("Invalid color")
        self.playerName = name
        self.playerColor = color