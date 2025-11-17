import sys

from stats import get_num_words
from stats import get_ch_dict
from stats import char_dict_to_sorted_list


def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    ch_dict = get_ch_dict(text)
    ch_sorted_list = char_dict_to_sorted_list(ch_dict)

    print_report(book_path, num_words, ch_sorted_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, ch_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in ch_sorted_list:
        if (item['char'].isalpha()):
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()

