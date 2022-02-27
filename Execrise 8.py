def print_word(word, number):
    new = []
    for i in range(number):
        new.append(word[i].upper())
    cool = len(word) - len(new)
    for num in range(cool):
        yup = number + num
        new.append(word[number + num])
    total = ""
    for i in range(len(word)):
        total = f"{total}{new[i]}"
    return total

    # for i in range

    # first_half = word[:number].upper()
    # second_half = word[number:]
    # return f"{second_half}{first_half}"


what_word = input("Enter word: ")
what_number = int(input("Enter number: "))
print(print_word(what_word, what_number))
