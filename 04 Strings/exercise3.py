#backward
str = input("Enter word: ")

for i in range(len(str), 0, -1):
    print(str[i-1])
