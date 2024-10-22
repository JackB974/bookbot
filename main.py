
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()       
    total_words = word_count(file_contents)
    letter_count = char(file_contents)

    print(total_words)
    print(letter_count)

def word_count(x):
    words = x.split()
    return len(words)

def char (text):
    char_dict = {}
    for letter in text.lower():
        if letter.isalpha():
            char_dict[letter] = char_dict.get(letter, 0) + 1
    for char in sorted(char_dict, key=lambda char: char_dict[char], reverse=True):
        print(f"The {char} character was found {char_dict[char]} times")

    return char_dict
if __name__ == "__main__":
    main()