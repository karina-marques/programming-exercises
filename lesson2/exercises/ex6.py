# Write a program to check whether a year is leap year or not.

x = int(input('Insert a year: '))

if x % 4 != 0:
    print (x, 'is a common year')
elif x % 100 != 0:
    print (x, 'is a leap year')
elif x % 400 != 0:
    print (x, 'is a common year')
else: 
    print (x, 'is a leap year')