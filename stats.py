def get_word_count(book):
    with open(book, 'r', encoding='utf-8') as f:
        text = f.read()
        return len(text.split())