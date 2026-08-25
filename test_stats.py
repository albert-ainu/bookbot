import unittest

from stats import chars_dict_to_sorted_list, get_chars_dict, get_num_words, sort_on


class TestGetNumWords(unittest.TestCase):
    def test_counts_simple_words(self):
        self.assertEqual(get_num_words("hello world"), 2)

    def test_ignores_extra_whitespace(self):
        self.assertEqual(get_num_words("  hello   world  \n"), 2)

    def test_empty_text_has_zero_words(self):
        self.assertEqual(get_num_words(""), 0)


class TestGetCharsDict(unittest.TestCase):
    def test_counts_each_character(self):
        self.assertEqual(get_chars_dict("Boot!"), {"b": 1, "o": 2, "t": 1, "!": 1})

    def test_uppercase_and_lowercase_share_one_count(self):
        self.assertEqual(get_chars_dict("Aa"), {"a": 2})

    def test_spaces_and_symbols_are_included(self):
        result = get_chars_dict("a b!")
        self.assertEqual(result[" "], 1)
        self.assertEqual(result["!"], 1)

    def test_empty_text_gives_empty_dict(self):
        self.assertEqual(get_chars_dict(""), {})


class TestSortOn(unittest.TestCase):
    def test_returns_the_count(self):
        self.assertEqual(sort_on(("b", 4868)), 4868)


class TestCharsDictToSortedList(unittest.TestCase):
    def test_sorts_greatest_to_least(self):
        result = chars_dict_to_sorted_list({"a": 1, "b": 3, "c": 2})
        self.assertEqual(result, [("b", 3), ("c", 2), ("a", 1)])

    def test_empty_dict_gives_empty_list(self):
        self.assertEqual(chars_dict_to_sorted_list({}), [])

    def test_does_not_modify_the_input_dict(self):
        original = {"a": 1, "b": 2}
        chars_dict_to_sorted_list(original)
        self.assertEqual(original, {"a": 1, "b": 2})


if __name__ == "__main__":
    unittest.main()
