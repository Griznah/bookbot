#!/home/linuxbrew/.linuxbrew/bin/python3

import sys
from stats import count_words, count_characters, sorted_list

def get_book_text(path):
    with open(path, 'r') as file:
        return file.read()

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    words = count_words(book_text)
    counts = count_characters(book_text)
    chars_sorted_list = sorted_list(counts)
    print_report(book_path, words, chars_sorted_list)


def print_report(book_path, words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()