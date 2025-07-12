import sys

try:
    app, file = sys.argv
    # raise Exception("Usage: python3 main.py <path_to_book>")
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



from stats import get_book_length, count_characters, sort_cgaracters

def get_book_text(path):
    # print(path)
    f = open(path)
    # print(f)
    line = f.read()
    
    return line

    
def main(path):
    # dir = "./books/"
    # path = dir+name
    text = get_book_text(path)
    num_words = get_book_length(text)
    chars = count_characters(text)
    sorted = sort_cgaracters(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted:
        print(f"{char["char"]}: {char["num"]}")
    # print(f"{num_words} words found in the document")
    # print(dictionary)


main(file)