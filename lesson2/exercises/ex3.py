# Write a program to check whether a number is negative, positive or zero.

x = float(input('Insert a number: '))


if x == 0:
    print (x, 'zero')   
elif x > 0:
    print (x, 'is positive')
else:
    print (x, 'is negative')