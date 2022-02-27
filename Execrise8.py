def print_word(words, numbers):
    new_word = f"{words[:numbers].upper()}{words[numbers:len(words)]}"
    return new_word


word = input("Word: ")
number = int(input("Number: "))
print(print_word(word, number))
