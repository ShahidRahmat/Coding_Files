import math
bill = float(input("What was the bill amount? \n"))
people = int(input("How many people are there? \n"))
bpp = bill / people
tip = int((input("What percentage tip would you like to give? \n")))
bpt = (tip/100) * bpp + bpp
rbpt = "{:.2f}".format(bpt)
print(f"Each person has to pay ${rbpt}")