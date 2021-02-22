# Write a program to check whether a number is divisible by 5 and 11 or not.

x = int(input('Insert a number: '))

is_divisible_by_5 = x % 5 == 0 
is_divisible_by_11 = x % 11 == 0 

if is_divisible_by_5 and is_divisible_by_11:
    print (x, 'is divisible by 5 and 11')
elif is_divisible_by_5 and not is_divisible_by_11:
    print (x, 'is divisible only by 5')
elif is_divisible_by_11 and not is_divisible_by_5:
    print (x, 'is divisible only by 11')
else:
    print (x, 'is not divisible by 5 and 11')