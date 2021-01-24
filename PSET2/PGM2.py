# Variables for tip and tax
tip = 0.15
salesTax = 0.07

# Get user input for meal subtotal & calculate total accordinly
subtotal = float(input("Enter the meal total: $"))
totalTip = subtotal*tip
totalTax = subtotal*salesTax
total = subtotal + totalTip + totalTax

print(f"""
========================================
Subtotal:       {subtotal:.2f}
----------------------------------------
Tip:            {totalTip:.2f}
Sales Tax:      {totalTax:.2f}
----------------------------------------
Total:          {total:.2f}
========================================
""")
