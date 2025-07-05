def count_words(text):
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return f"{num_words} words found in the document"

def count_chars(text):
    lc_text = text.lower()
    char_dict = {}
    for char in lc_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
