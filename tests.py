import unittest
from main import islands

image1 = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1]
]

image_outcome1 = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1]
]

image2 = [
    [0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1]
]

image_outcome2 = [
    [0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 1]
]


class TestIslands(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(islands(image1), image_outcome1)
        self.assertEqual(islands(image2), image_outcome2)


if __name__ == '__main__':
    unittest.main()
