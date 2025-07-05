def count_words(text):
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return num_words

def count_chars(text):
    lc_text = text.lower()
    char_dict = {}
    for char in lc_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_char_dict(char_dict):
    char_sorted = list()
    for i in char_dict:
        char_sorted.append({"char": i, "num": char_dict[i]})
    char_sorted.sort(reverse=True, key=sort_on)
    return char_sorted
