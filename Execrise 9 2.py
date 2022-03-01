def longest_word(string_list):
    total = ''
    for i in range(len(string_list)):
        if len(total) < len(string_list[i]):
            total = string_list[i]
    return total


long_list = input("Enter list: ").split()
print(longest_word(long_list))
