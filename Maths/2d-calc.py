import math
fig = input("For which figure do you want to calculate ?")
if fig == "Square":
    no1 = float(input("Enter the length of the side "))
    type = input("What do you want to calculate ?")
    if type == "Area":
        print(no1**2)
    elif type =='Perimeter':
        print(4*no1)
    else:
        print("Invalid Type")
if fig == "Rectangle":
    l = float(input("Enter the length"))
    w = float(input("Enter the width"))
    type = input("What do you want to calculate ?")
    if type == "Area":
        print(l*w)
    elif type == "Perimeter":
        print(2*(l+w))
    else:
        print("Invalid Type")
