def two_numbers(number1, number2):
    total = number1 + number2
    return total


first_number = int(input("Enter the First number: "))
second_number = int(input("Enter the Second number: "))

print(f"Together, your numbers add to {two_numbers(first_number, second_number)}")
