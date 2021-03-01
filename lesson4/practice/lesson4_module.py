# Write a function 'convert_temperatures' that converts an input list containing
# the numbers inside the list to Fahrneit. If the input_list
# is null, convert the numbers from 0 to 100.
# Tip: you can use the 'celsius_to_fahrenheit' function developed in lesson 3

def convert_temperatures(input_list = None):
    if(input_list == None):
        input_list = range(0, 100)
    # TODO: write code here

# Write a function 'count_digits' that counts the number of digits of an integer number given in input
# Tip: our counting system is a base 10. Use this to your advantage: what happens when you
# divide a number by 10 multiple times?

# Write a function 'fibonacci' that returns the first n elements of the fibonacci sequence as a list.
# The fibonacci sequence is defined here: https://en.wikipedia.org/wiki/Fibonacci_number
# Tip: Use the append() method to add elements at the end of a list.
# More info here: https://docs.python.org/3/tutorial/datastructures.html

# Write a function that takes as input an integer n and returns the factorial of that number
# The factorial is defined here: https://en.wikipedia.org/wiki/Factorial

# Write a function 'is_prime' that takes as input an integer n and True if the number is 
# a prime, False, otherwise
# The definition of a prime number is here: https://en.wikipedia.org/wiki/Prime_number
# Tip: Use the is_divisible function written in lesson 3

# Write a function 'sum_list' that takes a list of numbers as input and returns
# the sum of all the elements in the list

# Write a function 'multiply_list' that takes a list of numbers as input and returns
# the product of all the elements in the list

# Write a function 'max_list' that takes a list of numbers as input and returns
# the largest value in the list
# Tip: you can use the 'maximum' function defined in lesson 3

# Write a function 'min_list' that takes a list of numbers as input and returns
# the smallest value in the list
# Tip: you can use the 'minimum' function defined in lesson 3

# Write a function 'count_ones' that takes a binary list as input
# (for example the list a = [1, 0, 0, 0, 1])
# And counts the max consecutive ones.

# Write a function 'shuffle_list' that takes a list of numbers as input
# and shuffles the list
# Tip: take a look at the function shuffle in the random module

# Write a function 'sort_list' to sort a list of numbers in incresing order
# Tip: take a look at the sorted() function in the python standard library
# https://docs.python.org/3/library/functions.html#sorted