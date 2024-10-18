main_text = "books/frankenstein.txt"


def main():
    contents = read()
    count = word_count()
    character_counts = character_count()
    print(contents)
    print("--- Begin report on", main_text, "---")
    print(" ")
    print("Word Count:")
    print(f"There are {count} words in this document.")
    print(" ")
    print("Character Count:")
    for char, count in character_counts.items():
        print(f"The '{char}' character was found {count} times.")
    print("--- End Report ---")


def read():
    with open(main_text) as f:
        file_contents = f.read()
    return file_contents

def word_count():
    with open(main_text) as f:
        file_contents = f.read()
        words = file_contents.split()
        stringcount = len(words)
    return stringcount

def character_count():
    char_count = {}
    with open(main_text) as f:
        file_contents = f.read()
        lower_contents = file_contents.lower()
        for char in lower_contents:
            char_count[char] = char_count.get(char, 0) +1
    return char_count

main()