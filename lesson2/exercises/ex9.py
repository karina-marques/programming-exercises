# Write a program that takes three coeffiecients a,b,c and solves the equation
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
# Use the program to solve the following equations:
# Equation 1: x^2 – 5x + 6 = 0 (expected two real solutions: 3 and 2)
# Equation 2: x^2 + 2x – 2 = 0 (expected two real solutions: -1 + sqrt(3) and -1 -sqrt(3))
# Equation 3: x^2 + 2x + 1 = 0. (expected one real solution: -1)
# Equation 4: x^2 + 2x + 2 = 0. (expexted 0 real solutions)

import math

print("This program solves the quadratic equation a*x^2 + bx + c = 0 in the real realm")

a = float(input('Insert the a coefficient: '))
b = float(input('Insert the b coefficient: '))
c = float(input('Insert the c coefficient: '))

# Find delta
delta = b**2 - 4*a*c

if delta>0:
    y = (-b + math.sqrt(delta)) / (2 * a)
    print(y)
    z= (-b - math.sqrt(delta)) / (2 * a)
    print(z)
elif delta ==0:
    y = -b / (2 * a)
    print(y)
else:
    print('no real solution')   