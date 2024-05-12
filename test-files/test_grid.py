import unittest
from grid import Grid

class TestGrid(unittest.TestCase):
    def test_valid_grid_creation(self):
        # Test valid grid creation with correct rows and columns
        grid = Grid(6, 7)
        self.assertEqual(grid.gridSize, (6, 7))

    def test_invalid_grid_creation(self):
        # Test invalid grid creation with negative rows and columns
        with self.assertRaises(ValueError):
            Grid(-1, 7)

        with self.assertRaises(ValueError):
            Grid(6, -1)

        # Test invalid grid creation with zero rows and columns
        with self.assertRaises(ValueError):
            Grid(0, 7)

        with self.assertRaises(ValueError):
            Grid(6, 0)

if __name__ == "__main__":
    unittest.main()