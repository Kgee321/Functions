def longest_word(string_list):
    longest = max(string_list, key=len)
    return longest


long_list = input("Enter list: ").split()
print(longest_word(long_list))
