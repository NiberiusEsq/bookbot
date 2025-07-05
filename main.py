from stats import count_words, count_chars, sort_char_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(get_book_text(sys.argv[1]))} total words")
        print("--------- Character Count -------")
        char_list = sort_char_dict(count_chars(get_book_text(sys.argv[1])))
        for i in char_list:
            if i["char"].isalpha():
                print(f"{i['char']}: {i['num']}")
        print("============= END ===============")
    return

main()
