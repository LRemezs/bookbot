from stats import get_num_words
from stats import get_unique_character_count
from stats import get_sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        content_as_string = f.read()
    return content_as_string


def main():
    string = get_book_text(book_path)
    word_count = get_num_words(string)
    dictionary = get_unique_character_count(string)
    sorted_list = get_sorted_list(dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(item)
    print("============= END ===============")

    return 

main()
