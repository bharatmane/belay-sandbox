import unittest

from app.slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_digits(self):
        self.assertEqual(slugify("Room 101"), "room-101")


if __name__ == "__main__":
    unittest.main()
