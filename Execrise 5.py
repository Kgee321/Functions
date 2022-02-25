def check_factor(num1, num2):
    if num1 % num2 == 0:
        return f"{num1} is a factor of {num2}"
    else:
        return f"{num1} is not a factor of {num2}"


first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))
print(check_factor(first_number, second_number))
