# Write a program that takes three coeffiecients a,b,c and solves the quation
# a*x^2 + bx + c = 0, in the real domain.
# Short algebraic recap
# To solve a quadratic equation you have to compute the quantity
# delta = b^2 - 4*a*c
# The equation has:
# 1. Two different real solutions when delta > 0. The solutions are:
# solution 1 = (-b + sqrt(delta)) / (2 * a)
# solution 2 = (-b - sqrt(delta)) / (2 * a)
# 2. One real solution when delta == 0. The solution is:
# solution = -b / (2 * a)
# 3. Zero real solution when delta < 0.
# In python the square root of a number can be done by importing the math module with the following instruction
# import math
# And then calling the function 
# x = math.sqrt(a)

print("This program solves the quadratic equation a*x^2 + bx + c = 0 in the real realm")

a = float(input('Insert the a coefficient: '))
b = float(input('Insert the b coefficient: '))
c = float(input('Insert the c coefficient: '))

# Program goes here