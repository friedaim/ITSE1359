# Monthly Sales Tax Calcuator
    # Assuming we're setting county and state sales taxes
    # to a static value not given by the user.
monthYear = ""
subtotal = 0.0
countyTax = .025
stateTax = .06
while True:
    monthYear = input("Enter the Month and Year (Month Year): ")
    try:
        subtotal = float(input("Enter the total "
        "collected in this month: $"))
    except:
        subtotal = float(input("Enter only the "
        "numerical total collected in this month: $"))
    break;
totalSale = subtotal/(1+(stateTax+countyTax))
totalStateTax = totalSale*stateTax
totalCountyTax = totalSale*countyTax

print(f"""
Month: {monthYear}
------------------------
Total Collected:  $ {subtotal:.2f}
Sales:            $ {totalSale:.2f}
County Sales Tax: $ {totalCountyTax:.2f}
State Sales Tax:  $ {totalStateTax:.2f}
Total Sales Tax:  $ {totalStateTax+totalCountyTax:.2f}
------------------------
""")
