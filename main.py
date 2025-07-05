from stats import count_words, count_chars

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()



def main():
    print(count_words(get_book_text("./books/frankenstein.txt")))
    print(count_chars(get_book_text("./books/frankenstein.txt")))
    return

main()
