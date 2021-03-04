# 0. Write a function 'integer_multiplication_by_addition' that takes two integer numbers
# as input and performs the multiplication by doing subsequent additions
# For example integer_multiplication_by_addition(5,3) would do:
# 5 + 5 + 5 = 15
# Make sure that the function works normally also for negative numbers
# Also, perform a check on the inputs, veryfing that they are integers
# You can use isinstance(variable, int) to verify that variable is an integer
# More info here:  https://docs.python.org/3/library/functions.html

# 0. Write a function 'division_by_subtraction' that takes two integer numbers
# as input and performs the integer division by doing subsequent difference
# Make the function return a tuple of the type (result, remainder)
# For example division_by_subtraction(10,3) would do:
# 10 - 3 = 7
# 7 - 3 = 4
# 4 - 3 = 1
# 3 substractions performed
# value returned = (3, 1)
# Check that the divisor is not zero
# Check that the number in input to the function are integers
# This program has to work with negative numbers as well

# 2. Write a function 'count_integer_digits' that counts the number of digits of an integer number given in input
# Tip: our counting system is a base 10. Use this to your advantage: what happens when you
# divide a number by 10 multiple times?

# 1. Write a function 'convert_temperatures' that converts an input list containing
# the numbers inside the list to Fahrneit. If the input_list
# is null, convert the numbers from 0 to 100.
# Tip: you can use the 'celsius_to_fahrenheit' function developed in lesson 3

def convert_temperatures(input_list = None):
    if(input_list == None):
        input_list = range(0, 100)
    # TODO: write code here

# 3. Write a function 'fibonacci' that returns the first n elements of the fibonacci sequence as a list.
# The fibonacci sequence is defined here: https://en.wikipedia.org/wiki/Fibonacci_number
# Tip: Use the append() method to add elements at the end of a list.
# More info here: https://docs.python.org/3/tutorial/datastructures.html

# 4. Write a function that takes as input an integer n and returns the factorial of that number
# The factorial is defined here: https://en.wikipedia.org/wiki/Factorial

# 5. Write a function 'is_prime' that takes as input an integer and returns True if the number is 
# a prime, False, otherwise
# The definition of a prime number is here: https://en.wikipedia.org/wiki/Prime_number
# Tip: Use the is_divisible function written in lesson 3

# 6. Write a function 'is_perfect' that takes as input an intenger and returns True if the number
# is a perfect number, False otherwise.
# The definition of a perfect number is here: https://en.wikipedia.org/wiki/Perfect_number
# Tip: You have to find all the divisors of the number in input

# 7. Write a function 'sum_list' that takes a list of numbers as input and returns
# the sum of all the elements in the list

# 8. Write a function 'multiply_list' that takes a list of numbers as input and returns
# the product of all the elements in the list

# 9. Write a function 'max_list' that takes a list of numbers as input and returns
# the largest value in the list
# Tip: you can use the 'max()' function of Python to compare numbers

# 10. Write a function 'min_list' that takes a list of numbers as input and returns
# the smallest value in the list
# Tip: you can use the 'min()' function of Python to compare numbers

# 11. Write a function 'count_ones' that takes a binary list as input
# (for example the list a = [1, 0, 0, 0, 1])
# And counts the max number of consecutive ones.

# 12. Write a function 'shuffle_list' that takes a list of numbers as input
# and shuffles the list
# Tip: take a look at the function shuffle in the random module

# 13. Write a function 'sort_list' to sort a list of numbers in incresing order
# Tip: take a look at the sorted() function in the python standard library
# https://docs.python.org/3/library/functions.html#sorted