# 6.  A program that takes as input the quantity of flour expressed in grams and a percentage (e.g. a number between 0 and 100) that represents the quantity of water to use, and computes the water amount in grams

x= input('Quantity of flour (g):')
y= float(input('Hydratation degree (%):'))
if y >= 0 and y <= 100:
    z=(x*y)/100
    print (z, 'Water amount (g)')
elif y > 100 and <= 200:
    print("What exactly are you planning to do my friend")
else:
    print("You are a lost cause")