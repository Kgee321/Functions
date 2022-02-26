def number_in_list(list1, multiple):
    list2 = []
    for i in list1:
        i = int(i)
        if i % multiple == 0:
            list2.append(i)
    return list2


list_of_numbers = input("Put in your list of numbers: ").split()
number = int(input("Enter a number: "))
print(f"{number_in_list(list_of_numbers, number)} are factors of {number}")
