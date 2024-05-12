import unittest
from color import Color

class TestColor(unittest.TestCase):
    def test_valid_colors(self):
        # Test valid colors (red and yellow)
        red = Color(255, 0, 0)
        yellow = Color(255, 255, 0)

        self.assertEqual(red.red, 255)
        self.assertEqual(red.green, 0)
        self.assertEqual(red.blue, 0)

        self.assertEqual(yellow.red, 255)
        self.assertEqual(yellow.green, 255)
        self.assertEqual(yellow.blue, 0)

    def test_invalid_colors(self):
        # Test invalid colors
        with self.assertRaises(ValueError):
            # Invalid color: green (not red or yellow)
            Color(0, 255, 0)

        with self.assertRaises(ValueError):
            # Invalid color: blue (not red or yellow)
            Color(0, 0, 255)

if __name__ == "__main__":
    unittest.main()