def get_word_count(book):
    with open(book, 'r', encoding='utf-8') as f:
        text = f.read()
        return len(text.split())

def get_character_count(book):
    with open(book, 'r', encoding='utf-8') as f:
        text = f.read().lower()
        char_count = {}
        for char in text:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count

def sort_character_counts(char_count):
    sorted_counts = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return [{'character': char, 'count': count} for char, count in sorted_counts]
