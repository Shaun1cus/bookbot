from stats import get_word_count, get_character_count

def main():
    book = 'books/frankenstein.txt'
    num_words = get_word_count(book)
    print(f'{num_words} words found in the document')
    # print dictionary with character counts
    char_count = get_character_count(book)
    print(f'Character counts: {char_count}')

main()