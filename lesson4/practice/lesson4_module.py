# 0. Write a function that takes any number of inputs
# and returns True if all the inputs are integers.
# You can use isinstance(variable, int) to verify that variable is an integer
# More info here:  https://docs.python.org/3/library/functions.html
# To define a function with variable number of arguments, you can use the
# *args special argument in the function definition.
# More info here:
# https://www.geeksforgeeks.org/args-kwargs-python/

# 1. Write a function that takes two inputs
# and returns True if the inputs are suited for an integer division
# Two inputs are suited for an integer division if
# a. They are both integers
# b. The second input is different from 0
# Tip: Reuse the function of ex0 for the input check

# 2. Write a function that takes two integer numbers
# as input and returns the multiplication of the two numbers
# You cannot use the * operator
# Tip #0: Reuse the function of ex0 for the input check
# Tip #1: What is a multiplication between integers?
# Tip #2: Make sure that the function works normally also for negative numbers

# 3. Write a function that takes two integer numbers
# as input and performs the integer division among them.
# You cannot use the // and % operators
# Make the function return a tuple of the type (result, remainder)
# Tip #0: Reuse the function of ex1 for the input check
# Tip #1: What is a division between integers?
# Tip #2: Make sure that the function works normally also for negative numbers

# 4. Write a function that counts the number of digits of an integer number given in input
# Tip: our counting system is a base 10. Use this to your advantage: what happens when you
# perform the integer division between a number and 10 multiple times?

# 5. Write a function that converts an input list containing
# the numbers inside the list to Fahrneit. If the input_list
# is null, convert the numbers from 0 to 100.
# Tip: you can use the 'celsius_to_fahrenheit' function developed in lesson 3

# 6. Write a function that returns the first n elements of the fibonacci sequence as a list.
# The fibonacci sequence is defined here: https://en.wikipedia.org/wiki/Fibonacci_number
# Tip: Use the append() method to add elements at the end of a list.
# More info here: https://docs.python.org/3/tutorial/datastructures.html

# 7. Write a function that takes as input an integer n and returns the factorial of that number
# The factorial is defined here: https://en.wikipedia.org/wiki/Factorial

# 8. Write a function that takes as input an integer and returns True if the number is 
# a prime, False, otherwise
# The definition of a prime number is here: https://en.wikipedia.org/wiki/Prime_number
# Tip: Use the is_divisible function written in lesson 3

# 9. Write a function that takes as input an intenger and returns True if the number
# is a perfect number, False otherwise.
# The definition of a perfect number is here: https://en.wikipedia.org/wiki/Perfect_number
# Tip: You have to find all the divisors of the number in input

# 10. Write a function that takes a list of numbers as input and returns
# the sum of all the elements in the list

# 11. Write a function that takes a list of numbers as input and returns
# the product of all the elements in the list

# 12. Write a function that takes a list of numbers as input and returns
# the largest value in the list
# Tip: you can use the 'max()' function of Python to compare numbers

# 13. Write a function that takes a list of numbers as input and returns
# the smallest value in the list
# Tip: you can use the 'min()' function of Python to compare numbers

# 14. Write a function that takes a binary list as input
# (for example the list a = [1, 0, 0, 0, 1])
# And counts the max number of consecutive ones.

# 15. Write a function that takes a list of numbers as input
# and shuffles the list
# Tip: take a look at the function shuffle in the random module

# 16. Write a function to sort a list of numbers in incresing order
# Tip: take a look at the sorted() function in the python standard library
# https://docs.python.org/3/library/functions.html#sorted