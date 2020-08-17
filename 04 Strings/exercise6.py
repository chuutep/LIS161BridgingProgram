def count(word, char):
    char_count = 0
    for c in word:
        if c == char:
            char_count += 1
        return char_count

word = input("Enter word: ")
char = input("Enter char: ")

print(word.count(char))
