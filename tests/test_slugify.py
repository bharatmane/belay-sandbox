import unittest

from app.slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_has_docstring(self):
        self.assertIsInstance(slugify.__doc__, str)
        self.assertTrue(slugify.__doc__.strip())


if __name__ == "__main__":
    unittest.main()
