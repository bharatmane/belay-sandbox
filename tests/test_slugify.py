import unittest

from app.slugify import slugify


class SlugifyTest(unittest.TestCase):
    def test_words(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_caps_length_at_50(self):
        self.assertLessEqual(len(slugify("a" * 80)), 50)

    def test_never_ends_with_hyphen(self):
        text = "a" * 49 + " bbb"
        result = slugify(text)
        self.assertLessEqual(len(result), 50)
        self.assertFalse(result.endswith("-"))


if __name__ == "__main__":
    unittest.main()
