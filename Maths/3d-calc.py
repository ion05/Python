import math
fig = input("For which figure do you want to calculate ?")
if fig == "Cube":
    s = float(input("Enter the length of the side"))
    type = input("What do you want to calculate")
    if type == "LSA":
        print(4*s*s)
    elif type == "TSA":
        print(6*s*s)
    elif type == "Volume":
        print(s**3)
    else:
        print("Invalid Type")
