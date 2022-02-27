def make_positive(number):
    if number < 0:
        positive = number * -1  # or positive = abs(number)
        return positive
    else:
        return number


question = int(input("What is you number: "))
print(make_positive(question))
