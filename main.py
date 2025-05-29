import sys
from stats import get_num_words, get_char_count, get_char_count_report


def get_book_text(path_to_book):
    with open(path_to_book, "r") as f:
        contents = f.read()

    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]
    book_content = get_book_text(path_to_book)
    num_words = get_num_words(book_content)
    char_count = get_char_count(book_content)
    char_count_report = get_char_count_report(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in char_count_report:
        _char = c["char"]
        if _char.isalpha():
            print(f"{_char}: {c["num"]}")
    print("============= END ===============")


main()