"""Program for selling Movie Ticket at a cinema -- V2 to keep track of tickets sold
 Created by Katelyn Gee
 7/03/2022
 """


def main_function():

    # End function -- shows total sales
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
            print()
            main_function()

        # number of tickets they are selling of that type of ticket
        number = int(input(f"How many {ticket} ticket's do you want to sell? "))

        # confirming if they want that ticket
        confirm = input(f"Confirm purchase of {number} {ticket} ticket/s? (Y/N) ").lower()
        if confirm == "y":
            if ticket == "A":
                total += 12.5 * number
                adult += number
            if ticket == "S":
                total += 9 * number
                student += number
            if ticket == "C":
                total += 7 * number
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


# Main function
print("*************** Movie Ticket buying **********************")
main_function()
