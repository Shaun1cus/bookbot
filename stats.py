def get_word_count(book):
    with open(book, 'r', encoding='utf-8') as f:
        text = f.read()
        return len(text.split())

# Add a new function that takes the text from the book as a string,
# and returns the number of times each character, including symbols and
# spaces, appears in the string. Use a dictionary to store the counts.
# Convert any character to lowercase using .lower() before counting.
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
