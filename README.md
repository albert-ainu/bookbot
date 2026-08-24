# BookBot

BookBot is my first [Boot.dev](https://www.boot.dev) project: a small command-line
tool that analyzes a plain-text book and prints a report with the total word count
and how often each letter appears.

## Requirements

- Python 3.9 or newer (no third-party dependencies)

## Usage

```sh
python3 main.py <path_to_book>
```

For example:

```sh
python3 main.py books/frankenstein.txt
```

If no path is given, the program prints usage instructions and exits with status `1`.

## Example output

```text
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

## Project structure

```text
.
├── books/        # plain-text books to analyze
├── main.py       # CLI entry point and report formatting
├── stats.py      # word counting, character counting, and sorting
└── README.md
```

## How it works

1. `get_book_text` reads the file at the given path.
2. `get_num_words` counts whitespace-separated words.
3. `get_chars_dict` counts every character, lowercased.
4. `chars_dict_to_sorted_list` converts that dict into `(character, count)` pairs
   sorted from most to least frequent.
5. `print_report` prints the report, skipping non-alphabetic characters with
   `str.isalpha()`.

## Books

The books in `books/` are public-domain texts from [Project Gutenberg](https://www.gutenberg.org/).
