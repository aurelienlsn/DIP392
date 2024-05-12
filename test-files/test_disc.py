import unittest
from disc import Disc
from color import Color

class TestDisc(unittest.TestCase):
    def test_valid_disc_creation(self):
        # Test valid disc creation with color
        red_color = Color(255, 0, 0)
        disc_with_color = Disc(red_color)

        self.assertEqual(disc_with_color.discColor, red_color)

    def test_invalid_disc_creation(self):
        # Test invalid disc creation without color
        with self.assertRaises(ValueError):
            Disc(None)

if __name__ == "__main__":
    unittest.main()