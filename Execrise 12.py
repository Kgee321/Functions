"""
Block comment
Put unwanted code and notes in here
YAY

"""


def end(cost, ad, st, ch, gv):
    total_ticket = ad + st + ch + gv
    print("="*50)
    print(f"The total tickets brought today was {total_ticket}")
    print(f"""This was made up of: 
{ad} for Adults ,
{st} for Students
{ch} for Children
{gv} for Gift Vouchers """)
    print(f"Sale for today comes to {cost:,.2f}")
    print("="*50)


adult = 0
student = 0
child = 0
gift = 0
total = 0

yes_or_no = input("Do you want to buy a ticket? (Y/N) ").lower()
while yes_or_no == "y":
    ticket = input("""What type of ticket do you want to buy?
A for Adult, or
S for Student, or 
C for Child, or 
G for Gift voucher
""").upper()
    confirm = input(f"Confirm purchase of {ticket} ticket? (Y/N) ").lower()
    if confirm == "y":
        if ticket == "A":
            total += 12.5
            adult += 1
        if ticket == "S":
            total += 9
            student += 1
        if ticket == "C":
            total += 7
            child += 1
        if ticket == "G":
            gift += 1
    print()
    yes_or_no = input("Do you want to buy another ticket? (Y/N) ").lower()

if yes_or_no == "n":
    end(total, adult, student, child, gift)
