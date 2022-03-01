def total(x):
    if x > 30:
        fine = 30.00
    else:
        fine = (0.8 * x) + 0.5
    return f"Fine is ${fine:,.2f}"


overdue = int(input("Enter days overdue: "))
print(total(overdue))
