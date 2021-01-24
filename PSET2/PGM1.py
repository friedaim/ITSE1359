# Sales Tax Program
# Variables used for tax calculation
countyTax = 0.02
stateTax = 0.04

# Ask for pruchase total before taxes.
subtotal = float(input("Enter the total: $"))

# Totals with taxes
stateTaxTotal = subtotal*stateTax
countyTaxTotal = subtotal*countyTax
total = subtotal + stateTaxTotal + countyTaxTotal

print(f"""
========================================
Subtotal:           {subtotal:.2f}
----------------------------------------
State Tax:          {stateTaxTotal:.2f}
County Tax:         {countyTaxTotal:.2f}
----------------------------------------
Total Sales Tax:    +{stateTaxTotal+countyTaxTotal:.2f}
Total:              {total:.2f}
========================================
""")
