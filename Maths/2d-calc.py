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
