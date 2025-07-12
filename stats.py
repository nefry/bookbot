def get_book_length(text) :
    return(len(text.split()))

def get_alphabet():
    a=[]
    for let in range(ord("a"),ord("z")+1):
       a.append(chr(let))
    return a

def count_characters(text):
    str = text.lower()
    letters = get_alphabet()
    dictionary = {}
    for letter in letters:
        dictionary[letter]=str.count(letter)

    return dictionary

def sort_on(items):
    return items["num"]

def sort_cgaracters(d):
    sorted=[]
    myKeys = list(d.keys())
    for key in myKeys:
        sorted.append({"char":key, "num":d[key]})
    # print(sorted)
    sorted.sort(reverse=True,key=sort_on)
    return sorted