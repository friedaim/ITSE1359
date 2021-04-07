# Program to streamline calculations for an ISP.

pkgOptions = ["A", "B", "C"]

def getPackage():
    pkg = input("Enter the package the customer currently has (A, B, or C) or type 'exit' to leave: ")
    return pkg

def validPackage():
    # if(pkg not in options):
    pkg = ''
    while True:
        try:
            pkg = getPackage().upper()
        except KeyboardInterrupt:
            exit()
        if pkg in pkgOptions or pkg == 'EXIT':
            break
        else:
            print("Enter only A, B, or C. Or Type 'exit' to leave the application.")
    return pkg

def getHours():
    hours = input("How many hours did they use over the entire month? ")
    return hours

def validHours():
    hours = 0
    while True:
        error = False
        try:
            hours = int(getHours())
        except KeyboardInterrupt:
            exit()
        except:
            print("Enter only a numeric value between 720 and 0 hours.")
            error = True
        if 0<hours<720:
            break
        elif not error:
            print("Enter only a numeric value between 720 and 0 hours.")
    return hours

def calculatePkg(pkg, hours):
    # Function to calc pack
    if pkg == 'A':
        total = 15+(hours-50)*2 if((hours-50)*2)>0 else 15
        return total
    if pkg == 'B':
        total = 20 + (hours - 100) * 1.50 if ((hours - 100) * 1.50) > 0 else 20
        return total
    if pkg == 'C':
        total = 25 + (hours - 150) * 1 if ((hours - 150) * 1) > 0 else 25
        return total


def main():
    # Main run
    run = True
    while run:
        pkg = validPackage()
        if(pkg=='EXIT'):
            run = False
            exit()
        hours = validHours()
        total = calculatePkg(pkg, hours)
        print(f"""
      Customer Bill Summary
----------------------------------
|{'Package':^10}|{'Hours':^10}|{'Total':^10}|
|{pkg:^10}|{hours:^10}|{total:^10}|
        """)

if __name__=="__main__":
    main()