# Program to calculate loan interest,
# monthly payment, and overall loan payment.

def calcLoan(yrRate,term,amt):
    monthRate = yrRate/12
    paymentNum = (pow(1+monthRate,term)*monthRate)
    paymentDen = (pow(1+monthRate,term)-1)
    payment = (paymentNum/paymentDen)*amt
    paybackAmt = payment*term
    totalInterest = paybackAmt-amt

    print(f"""
    Loan Amount:                    ${amt}
    Annual Interest Rate:           {round(yrRate*100,2)}%
    Number of Payments:             {term}
    Montly Payment:                 ${round(payment,2)}
        Amount Paid Back:           ${round(paybackAmt,2)}
        Interest Paid:              ${round(totalInterest,2)}""")

print("Loan Calculator Program- Type 'help' for help.")
while True:
    command = input("Enter Command: ")
    if(command=="exit"): break
    # Help menu
    if(command=="help"):
        print("""
    -----------
    Available commands:
    'help' - displays this menu
    'loan' - calculate a loan payment
    'exit' - leave the program
    -----------
    """)

    # Loan calculations and input validation
    if(command == "loan"):
        rate = 0
        term = 0
        amount = 0
        while True:
            # Use try catch for taking only the corrent input
            try:
                rate = float(input("What is the yearly interest rate? "))
            except:
                continue
            break
                #rate = float(input("What is the yearly interest rate? "
                 #"(exclude % sign) "))
        while True:
            try:
                term = int(input("What is the loan term (months)? "))
            except:
                continue
            break
        while True:
            try:
                amount = float(input("What is the total amount for the loan? $"))
            except:
                continue
            break
        rate = rate/100
        calcLoan(rate,term,amount)
