

print("Welcome to the tip calculator")
bill = float(input("What was the total bill?"))
totalPeople = int(input ("How many people to split the bill?"))
percent = int(input("what percentage tip would you like to give?"))

total = float((bill+(bill*percent/100))/totalPeople)
print("%.2f" % total)