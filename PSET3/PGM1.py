# Property Tax Calculation Program
propVal = input("Enter the actual value of the property: $")
while True:
    try:
        propVal = float(propVal)
    except:
        propVal = float(input("Enter only the numerical value"
         "of the property: $"))
    break

assessVal = propVal * 0.6
propTax = (assessVal/100) * .75

print(f"Assessment Value: $ {assessVal:.2f}")
print(f"Property Tax:     $ {propTax:.2f}")
