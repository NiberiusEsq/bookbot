def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def count_words(text):
    words = text.split()
    num_words = 0
    for word in words:
        num_words += 1
    return f"{num_words} words found in the document"

def main():
    print(count_words(get_book_text("./books/frankenstein.txt")))
    return

main()
