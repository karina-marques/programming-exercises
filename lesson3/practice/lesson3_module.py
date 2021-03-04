# Write the functions you will use in the exercises here
# In the single exercises write just the test cases
# That will use the functions defined in this module.

# 1. Write a function named 'celsius_to_fahrenheit' that takes as input a temperature in C 
# and outputs the temperature converted into Fahrenheit
def celsius_to_fahrenheit(temperature_in_celsius):
    return 32+temperature_in_celsius*180/100

# 2. Write a function named 'fahrenheit_to_celsius' that takes as input a temperature in F and outputs the temperature converted it into C
def fahrenheit_to_celsius(temperature_in_fahrenheit):
    return (temperature_in_fahrenheit-32)*100/180

# 3. Write a function named 'celsius_to_kelvin' that takes as input a temperature in C and outputs the temperature converted it into Kelvin
def celsius_to_kelvin(temperature_in_celsius):
    return temperature_in_celsius+273.15

# 4. Write a function named 'fahrenheit_to_kelvin' that takes as input a temperature in F and outputs the temperature converted it into Kelvin
# Tip: reuse the previous functions.
def fahrenheit_to_kelvin(temperature_in_fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(temperature_in_fahrenheit))

# 5. Write a function named 'minimum' that takes as input two numbers and returns the minimum
def minimum(a,b):
    if a <= b: #what if is a equal to b?
        return a
    return b

# 6. Write a function named 'maximum' that takes as input two numbers and returns the maximum
def maximum(a,b):
    if a >= b:
        return a
    return b

# 7. Write a function named 'maximum3' that takes as input three numbers and returns the maximum
# Tip: reuse the function 'maximum' previously defined
def maximum3(a,b,c):
    return maximum(maximum(a,b),c)

# 8. Write a function named 'is_dividible' that takes as input two integer numbers 'a' and 'b' and returns True if a is dividible by b and False otherwise.
# Where is the output of this function?
# Read again the passage about not printing inside functions unless necessary
def is_divisible(a,b):
    return a % b == 0

# 9. Write a function named 'is_even' that takes as input an integer number and returns True if the number is Even and False otherwise
# Tip: reuse the function 'is_dividible'
def is_even(a):
    return is_divisible(a,2)

# 10. Write a function named 'is_leap_year' that takes as input an integer number and returns True if the number corresponds to a Leap year in the Gregorian Calendar, False otherwise
# Tip: reuse the function 'is_dividible'
# The correct chain is in lesson2/ex6.py
def is_leap_year (a):
    if not is_divisible(a,4):
        return False
    elif not is_divisible(a,100):
        return True
    elif not is_divisible(a,400):
        return False
    else:
        return True

# 11. Write a function named 'compute_circle_area' that takes as input a number representing
# the radius of a circle and computes the area of a circle.
# Tip: The area of a circle equation is available here: https://en.wikipedia.org/wiki/Area_of_a_circle
# You can found pi in the math module: https://docs.python.org/3/library/math.html#constants

# 12. Write a function named 'toss_dice' that simulates the toss of a dice with 6 sides
# Hint: Check the functions
# - random.seed(a=None, version=2)
# - random.randint(a, b) 
# On the random module documentation https://docs.python.org/3/library/random.html