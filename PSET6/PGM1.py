# Program with menu interface to determine how far an object is
mediums = {
"carbon dioxide":258.0,
"air":331.5,
"helium":972.0,
"hydrogen":1270.0
}

inputMedium = ""
inputTime = 0
distance = 0 # in meters

def help():
    print("""
    Enter a command below
    ------------------------
    Help - this menu
    ------------------------
    Carbon Dioxide
    Air
    Helium
    Hydrogen
    ------------------------
    Exit - exit
    ------------------------""")

# Begin runtime code
print("Calculate how far an object is based on the medium and time "
"sound traveled through.")
help()
while True:
    while True:
        try:
            inputMedium = input("What is the medium the sound traveled through? ").lower()
            if(inputMedium in mediums):
                # Input validated for medium used.
                break
            elif(inputMedium=="help"):
                print("Please enter one of the commands below.")
                help()
            elif(inputMedium=="exit"):
                print("Bye")
                exit()
            else:
                help()
                continue
        except KeyboardInterrupt:
            print("Bye")
            exit()
    while True:
        try:
            inputTime = int(input("How many seconds did it take to travel "
             "from the source to the destination? "))
            if(inputTime>=0 and inputTime<=30): break
            else: print("Enter only a numeric value between 0 and 30 seconds.")
        except KeyboardInterrupt:
            print("Bye")
            exit()
        except:
            print("Enter only a numeric value between 0 and 30 seconds.")
            continue
    # All input values should properly validated by here
    distance=mediums[inputMedium]*inputTime

    print(f"""
        ------------------------
        Results
        ------------------------
        Distance: {distance} m
        Medium: {inputMedium}
        Time: {inputTime} s
        ------------------------""")
