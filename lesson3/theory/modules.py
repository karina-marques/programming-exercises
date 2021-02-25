# A module in python is collection of functions, classes, variables and constants
# Modules can be imported into the code using the import keyword
# Imports are usually placed at the top of your source file, so they are all in the same place

import math 

# Imports the standard python math module, which contains useful functions for mathematical processing
# For example, the function sqrt(x) is available only in the math module.
# Documentation for the math module is here https://docs.python.org/3/library/math.html

import random

# Imports the standard python random module, that you can use to generate
# Aleatory variables and random number
# Documentation for the random module is here https://docs.python.org/3/library/random.html

# Once you have imported a module, you can access to the functions it defines using the . operator, for example

number0 = 5
number0b = 7
print("The square root of", number0, "is", math.sqrt(number0)) # module_name.function_name
print("The square root of", number0b, "is", math.sqrt(number0b)) # module_name.function_name

# You can specify an alias for the module with the 'as' keyword like this
import math as mt
number0 = 5
number0b = 7
print("The square root of", number0, "is", mt.sqrt(number0)) # module_alias_name.function_name
print("The square root of", number0b, "is", mt.sqrt(number0b)) # module_alias_name.function_name

# Sometimes you will see imports with a different syntax, for example
from math import fabs
# fabs(x) is a function of the math module that takes a number x as input
# and returns the absolute value of x.
# This syntax is importing only the function fabs from the math module.
# When you use this syntax, you can use fabs like this
number1 = 5
number2 = -5

print("The absolute value of", number1, "is", fabs(number1)) # module name is not specified!
print("The absolute value of", number2, "is", fabs(number2)) # module name is not specified!

# This syntax is useful to reduce verbosity, but it can create confusion.
# You do not know in which module is the fabs function defined.

# Python standard library has a lot of useful modules
# You should always check if a function that is doing what you need is already defined in some module
# to avoid re-inventing the wheel.

# Defining a module is pretty easy. Each python file is actually a module.
# The file name is the module identifier.
# For example if you have a file named:
# mathematics.py
# That defines some mathematical functions
# You can import it in another file by doing
'''import mathematics'''