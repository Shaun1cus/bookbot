def main():
    book = 'books/frankenstein.txt'
    text = get_book_text(book)
    print(text)
def get_book_text(book):
    with open(book, 'r', encoding='utf-8') as f:
        return f.read()

main()