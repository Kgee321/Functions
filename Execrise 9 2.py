def longest_word(string_list):
    total = ['']
    for i in range(len(string_list)):
        if len(total[0]) < len(string_list[i]):
            total = [string_list[i]]
        elif len(total[0]) == len(string_list[i]):
            total.append(string_list[i])
    return total


long_list = input("Enter list: ").split()
print(f"longest words in list is {longest_word(long_list)}")
