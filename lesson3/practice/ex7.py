# Write here the test case for 'is_divisible' function
# Write in this file a function to help with the output
# For example a function is_divisible_string
# that takes as input two integer numbers (let's call them x and y)
# and returns "x is divisible by y" if x is divisible by y and
# "x is not divisible by y" if x is not divisible by y

import lesson3_module

def is_divisible_string(x,y):
    if lesson3_module.is_divisible(x,y):
        return str(x) + " is divisible by " + str(y)
    return str(x) + " is not divisible by " + str(y)

x= int(input('Insert a number:'))
y= int(input('Insert a number:'))

print(is_divisible_string(x,y))