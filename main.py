def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted = dict(sorted(chars_dict.items(), reverse = True, key=lambda x: x[1]))   
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n\n")
    for letter in chars_sorted:
        print(f"The {letter} character was found {chars_sorted[letter]} times")
    print(f"\n--- End report ---")



def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(file_string):
    words = file_string.split()
    return len(words)

def get_chars_dict(file_string):
    dict_count = dict()
    lower_words = file_string.lower().split()
    for word in lower_words:
        for letter in word:
            if letter.isalpha() == True:
                if letter not in dict_count:
                    dict_count[letter] = 1
                else:
                    count = dict_count[letter]
                    dict_count[letter] = count + 1
    return dict_count 



main()
