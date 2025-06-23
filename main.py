def main():
    book = 'books/frankenstein.txt'
    text = get_book_text(book)
    num_words = len(text.split())
    print(f'{num_words} words found in the document')
def get_book_text(book):
    with open(book, 'r', encoding='utf-8') as f:
        return f.read()

main()