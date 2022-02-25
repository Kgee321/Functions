def check_status(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 25:
        return "normal"
    elif 25 <= bmi < 30:
        return "overweight"
    elif bmi >= 30:
        return "obese"


num = int(input("What is your number: "))
print(f"You are {check_status(num)}")

