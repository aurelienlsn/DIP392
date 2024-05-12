import unittest
from player import Player

class TestPlayer(unittest.TestCase):
    def test_valid_color(self):
        player = Player("John", "red")
        self.assertEqual(player.playerColor, "red")

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            Player("Jane", "blue")

if __name__ == "__main__":
    unittest.main()