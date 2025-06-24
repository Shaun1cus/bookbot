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


# Add a new function that takes the dictionary of characters and
# their counts and returns a sorted list of dictionaries.
# Each dictionary should have two key-value pairs: one for the 
# character itself and one for that character's count.
# Sort the list from greatest to least by count.
def sort_character_counts(char_count):
    sorted_counts = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return [{'character': char, 'count': count} for char, count in sorted_counts]
