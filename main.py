from stats import get_word_count, get_character_count, sort_character_counts
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    num_words = get_word_count(book)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book}...')
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")
    sort_count = sort_character_counts(get_character_count(book))
    char_count = {item['character']: item['count'] for item in sort_count}
    for char, count in char_count.items():
        if char.isalpha():
            print(f'{char}: {count}')
    print("============= END ===============")

main()