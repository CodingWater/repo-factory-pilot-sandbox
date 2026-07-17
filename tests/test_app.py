import unittest

from app import slugify_title


class SlugifyTitleTests(unittest.TestCase):
    def test_normal_words(self):
        self.assertEqual(slugify_title("Hello World"), "hello-world")

    def test_mixed_case(self):
        self.assertEqual(slugify_title("MyTitle"), "mytitle")

    def test_surrounding_whitespace(self):
        self.assertEqual(slugify_title("  hello  "), "hello")

    def test_punctuation_collapse(self):
        self.assertEqual(slugify_title("Hello!!!---World"), "hello-world")

    def test_repeated_separators(self):
        self.assertEqual(slugify_title("a---b"), "a-b")

    def test_digits(self):
        self.assertEqual(slugify_title("Part 2"), "part-2")

    def test_empty_input(self):
        self.assertEqual(slugify_title(""), "")

    def test_no_alphanumeric_input(self):
        self.assertEqual(slugify_title("!!!---***"), "")

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            slugify_title(123)

    def test_unicode_not_lowercased_to_ascii(self):
        self.assertEqual(slugify_title("\u212a"), "")
        self.assertEqual(slugify_title("\u0130stanbul"), "stanbul")
