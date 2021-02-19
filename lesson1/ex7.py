# 7. Given a number X that express the consumption of a car in:
# X are the litres of gasoline used to drive 100 km
# Convert this number to a consumption expressed as:
# Z is the number of kilometers doable with 1 liter of gasoline

x= float(input('Consumption of the car (litres for 100km):'))
z=100/x 
print (round(z,2), 'km per litre (g)')