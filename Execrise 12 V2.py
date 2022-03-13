"""ProgramforsellingMovieTicketatacinema--V2tokeeptrackofticketssold
CreatedbyKatelynGee
7/03/2022
"""


def num_check(question, ticket):
while not VALID:
    try:
        number=int(input(question))
        if number<=0:
            print(ERROR)
        else:
            confirm_yes(number, ticket)
    except ValueError:
        print(ERROR)


def main_function():
    #Endfunction--showstotalsalesandtotaltickets
    def end(cost,ad,st,ch,gv):
    total_ticket= ad + st + ch + gv
    print("="*50)
    print(f"The total tickets sold today was{total_ticket}")
    print(f"""This was made up of:
    {ad} for Adults,
    {st} for Students
    {ch} for Children
    {gv} for GiftVouchers""")
    print(f"Salesforthedaycometo${cost:,.2f}")
    print("="*50)


    yes_or_no=input("Doyouwanttosellaticket?(Y/N)").lower()
    while yes_or_no =="y":
        ticket=input("""Whattypeofticketdoyouwant?
        AforAdult,or
        SforStudent,or
        CforChild,or
        GforGiftvoucher
        """).upper()

    #iftheyputinthewrongtypeofticket
        if ticket != "A"and ticket != "S" and ticket !="C" and ticket !="G":
            print("""Thatwasanincorrectticketsoithasbeencancelled,tryagainusingeither
            AforAdult,or
            SforStudent,or
            CforChild,or
            GforGiftvoucher""")

            print()
            main_function()

        #Checkingforvalidintegerandloopsuntiloneisentered
        num=f"Howmany{ticket}ticket'sdoyouwanttosell?"
        num_check(num,ticket,yes_or_no)


    defconfirm_yes(ticket,number,yes_or_no):
    #confirmingiftheywantthatticket

    whileyes_or_no=='y':
    confirm=input(f"Confirmpurchaseof{number}{ticket}ticket/s?(Y/N)").lower()
    #Startingamountofticketsforeachpossibleticket--Alwaysstartswith0
    adult=0
    student=0
    child=0
    gift=0
    total=0
    ifconfirm=="y":
    ifticket=="A":
    total+=ADULT_PRICE*number
    adult+=number
    ifticket=="S":
    total+=STUDENT_PRICE*number
    student+=number
    ifticket=="C":
    total+=CHILD_PRICE*number
    child+=number
    ifticket=="G":
    gift+=number
    elifconfirm=="n":
    print("Ok,Ticketasbeencancelled")
    else:
    print("Thatwaswronginput,tickethasbeencancelled,eitherbutYforyesorNforno:")
    main_function()
    print()
    yes_or_no=input("Doyouwanttosellanotherticket?(Y/N)").lower()

    ifyes_or_no=="n":
    end(total,adult,student,child,gift)
    elifyes_or_no!="n"or"y":
    print("Thatwaswronginput,eitherbutYforyesorNforno:")
    print()
    main_function()

#SetpriceofticketsforAdult,Student,andChild
ADULT_PRICE=12.5
CHILD_PRICE=7
STUDENT_PRICE=9

#Setvalueofothervariables
VALID=False
ERROR="Pleaseenteravalidinteger"

#Mainfunction
print("***************MovieTicketbuying**********************")
main_function()
