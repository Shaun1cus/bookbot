from stats import get_word_count, get_character_count, sort_character_counts

def main():
    book = 'books/frankenstein.txt'
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