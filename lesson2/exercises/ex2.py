# Write a program to find maximum between three numbers.

x = float(input('Insert values: '))
y = float(input('Insert values: '))
z = float(input('Insert values: '))

if x > y and x > z:
    print (x, 'Maximum value')   
elif y > z and y > x:
    print (y, 'Maximum value')
else:
    print (z, 'Maximum value')