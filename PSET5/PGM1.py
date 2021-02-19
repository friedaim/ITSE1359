# Program to determinpe freezinpg poinpt based on user inp

inp = ""
output = ""
freeze_eo = -173
freeze_mec = -38
freeze_ox = -362
freeze_o2 = 32
boil_eo = 172
boil_mec = 676
boil_ox = -306
boil_o2 = 212
while True:
    try:
        inp = float(input("What is the temperature? "))
        print(f"Temperature entered: {inp}")
        if(inp<=freeze_eo): output+="\nEthyl Alcohol will freeze"
        elif(inp>=boil_eo): output+="\nEthyl Alcohol will boil"
        if(inp<=freeze_mec): output+="\nMercury will freeze"
        elif(inp>=boil_mec): output+="\nMercury will boil"
        if(inp<=freeze_ox): output+="\nOxygen will freeze"
        elif(inp>=boil_ox): output+="\nOxygen will boil"
        if(inp<=freeze_o2): output+="\nWater will freeze"
        elif(inp>=boil_o2): output+="\nWater will boil"
        if(output==""):
            output="The temperature entered meets none of the "
            "criteria specified."
        print(output)
        break
    except KeyboardInterrupt:
        print("Goodebye.")
        break
    except:
        print("Only enter a numeric value!")
        continue
