# Program to calculate a person's body mass index (BMI).
# height in inches, weight in pounds

height = 0
weight = 0
BMIcalc = 0
result = ""
# For ease of use
def err(v):
    print(f"Enter only the numeric value of your {v}!")
def bye():
    print("Goodbye.")

while True:
    try:
        height = float(input("What is your height (inches)? "))
        if(height<0):continue
        break
    except KeyboardInterrupt:
        bye()
        break
    except:
        err("height")
        continue
    break
while True:
    try:
        weight = float(input("What is your weight (lbs)? "))
        if(weight<0):continue
        break
    except KeyboardInterrupt:
        bye()
        break
    except:
        err("weight")
        continue

BMIcalc = (weight*703)/(pow(height,2))

if(BMIcalc>18.5 and BMIcalc<=25): result = "optimal weight"
elif(BMIcalc<18.5): result = "underweight"
elif(BMIcalc>25): result = "overweight"

print(f"A person with a height of {height:.2f} inches and a weight of {weight:.2f} "
f"pounds has a Body Mass Index (BMI) of {BMIcalc:.2f} is considered {result}"
f", according health professionals.")
