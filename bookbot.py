def main():
    path = 'books/frankenstein.txt'
    with open(path) as file:
        contents = file.read()
        # words = contents.split()
        # words_count = len(words)
        letters_count = count_letters(contents)
        for letter in letters_count:
            print(f"The {letter[0]} character was found {letter[1]} times")

def count_letters(content):
    letters = {}
    content = content.lower()
    for c in content:
        if not c.isalpha():
            continue
        if c not in letters:
            letters[c] = 0
        letters[c] += 1
    return sorted(letters.items(), key=lambda x:x[1], reverse=True)

main()
