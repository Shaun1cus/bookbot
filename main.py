from stats import get_word_count

def main():
    book = 'books/frankenstein.txt'
    num_words = get_word_count(book)
    print(f'{num_words} words found in the document')

main()