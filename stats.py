def get_num_words(text: str) -> int:
    """Return the number of whitespace-separated words in the text."""
    return len(text.split())


def get_chars_dict(text: str) -> dict[str, int]:
    """Return how many times each (lowercased) character appears in the text."""
    chars: dict[str, int] = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(item: tuple[str, int]) -> int:
    """Sorting key: the count half of a (character, count) pair."""
    return item[1]


def chars_dict_to_sorted_list(num_chars_dict: dict[str, int]) -> list[tuple[str, int]]:
    """Turn a character-count dict into a list of pairs sorted by count, descending."""
    sorted_list: list[tuple[str, int]] = []
    for ch in num_chars_dict:
        sorted_list.append((ch, num_chars_dict[ch]))
    return sorted(sorted_list, reverse=True, key=sort_on)
