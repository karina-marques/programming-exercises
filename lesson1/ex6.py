# 6.  A program that takes as input the quantity of flour expressed in grams and a percentage (e.g. a number between 0 and 100) that represents the quantity of water to use, and computes the water amount in grams

x= float(input('Quantity of flour (g):'))
y= float(input('Hydratation degree (%):'))
z=(x*y)/100
print (z, 'Water amount (g)')