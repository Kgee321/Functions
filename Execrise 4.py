def starts_with_a(word):
    if word[0] == "A":
        return True
    else:
        return False


your_word = input("Enter word: ").strip().upper()
print(starts_with_a(your_word))


