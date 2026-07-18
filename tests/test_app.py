import unittest

from app import render_title_summary, slugify_title, validate_title


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


class ValidateTitleTests(unittest.TestCase):
    def test_ordinary_input(self):
        self.assertEqual(validate_title("Hello World"), "Hello World")

    def test_surrounding_whitespace_trimmed(self):
        self.assertEqual(validate_title("  hello  "), "hello")

    def test_whitespace_only_rejected(self):
        with self.assertRaises(ValueError):
            validate_title("   ")

    def test_non_string_rejected(self):
        with self.assertRaises(TypeError):
            validate_title(None)

    def test_exactly_80_chars_accepted(self):
        title = "a" * 80
        self.assertEqual(validate_title(title), title)

    def test_81_chars_rejected(self):
        title = "a" * 81
        with self.assertRaises(ValueError):
            validate_title(title)

    def test_internal_content_preserved(self):
        self.assertEqual(
            validate_title("  Hello, World! 123  "),
            "Hello, World! 123",
        )

    def test_empty_string_rejected(self):
        with self.assertRaises(ValueError):
            validate_title("")

    def test_trimmed_80_chars_with_padding_accepted(self):
        title = "a" * 78
        padded = " " + title + " "
        self.assertEqual(validate_title(padded), title)


class RenderTitleSummaryTests(unittest.TestCase):
    def test_ordinary_output(self):
        self.assertEqual(
            render_title_summary("  Hello, World!  "),
            "# Hello, World!\n\nSlug: `hello-world`",
        )

    def test_surrounding_whitespace_trimmed(self):
        self.assertEqual(
            render_title_summary("  hello  "),
            "# hello\n\nSlug: `hello`",
        )

    def test_heading_preserves_content(self):
        self.assertEqual(
            render_title_summary("  Hello, World! 123  "),
            "# Hello, World! 123\n\nSlug: `hello-world-123`",
        )

    def test_empty_slug_accepted(self):
        self.assertEqual(
            render_title_summary("!!!"),
            "# !!!\n\nSlug: ``",
        )

    def test_non_string_rejected(self):
        with self.assertRaises(TypeError):
            render_title_summary(None)

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            render_title_summary("")

    def test_whitespace_only_rejected(self):
        with self.assertRaises(ValueError):
            render_title_summary("   ")
