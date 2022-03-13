"""Program for selling Movie Ticket at a cinema -- V2 to keep track of tickets sold
 Created by Katelyn Gee
 7/03/2022
 """


def main_function():
    # End function -- shows total sales and total tickets
    def end(cost, ad, st, ch, gv):
        total_ticket = ad + st + ch + gv
        print("=" * 50)
        print(f"The total tickets sold today was {total_ticket}")
        print(f"""This was made up of: 
    {ad} for Adults ,
    {st} for Students
    {ch} for Children
    {gv} for Gift Vouchers """)
        print(f"Sales for the day come to ${cost:,.2f}")
        print("=" * 50)

    # Starting amount of tickets for each possible ticket -- Always starts with 0
    adult = 0
    student = 0
    child = 0
    gift = 0
    total = 0

    yes_or_no = input("Do you want to sell a ticket? (Y/N) ").lower()
    while yes_or_no == "y":
        ticket = input("""What type of ticket do you want?
A for Adult, or
S for Student, or 
C for Child, or 
G for Gift voucher
""").upper()

        # if they put in the wrong type of ticket
        if ticket != "A" and ticket != "S" and ticket != "C" and ticket != "G":
            print("""That was an incorrect ticket so it has been cancelled, try again using either 
A for Adult, or
S for Student, or 
C for Child, or 
G for Gift voucher""")
            ticket = ''
            print()
            main_function()

        # Checking for valid integer and loops until one is entered
        number = int(input(f"How many {ticket} ticket's do you want to sell? ")) # number of tickets they are selling of that type of ticket

        # confirming if they want that ticket
        confirm = input(f"Confirm purchase of {number} {ticket} ticket/s? (Y/N) ").lower()
        if confirm == "y":
            if ticket == "A":
                total += ADULT_PRICE * number
                adult += number
            if ticket == "S":
                total += STUDENT_PRICE * number
                student += number
            if ticket == "C":
                total += CHILD_PRICE * number
                child += number
            if ticket == "G":
                gift += number
        elif confirm == "n":
            print("Ok, Ticket as been cancelled")
        else:
            print("That was wrong input, ticket has been cancelled, either but Y for yes or N for no:")
            main_function()
        print()
        yes_or_no = input("Do you want to sell another ticket? (Y/N) ").lower()

    if yes_or_no == "n":
        end(total, adult, student, child, gift)
    elif yes_or_no != "n" or "y":
        print("That was wrong input, either but Y for yes or N for no:")
        print()
        main_function()


# Set price of tickets for Adult, Student, and Child
ADULT_PRICE = 12.5
CHILD_PRICE = 7
STUDENT_PRICE = 9

# Set value of other variables
VALID = False
ERROR = "Please enter a valid integer"

# Main function
print("*************** Movie Ticket buying **********************")
main_function()
