# A function is the most basic piece of reusable code

# You can think of a function as a box
# You provide the box some inputs
# The box works some black magic
# The box outputs something

# The set of a function inputs is known as function INPUTS or ARGUMENTS.
# The set of function inputs, name and outputs is known as function SIGNATURE or PROTOTYPE.
# The black magic happening inside of a function is known as function BODY
# The process of creating a new function in python, that is write both the function signature
# and function body, is known as function DEFINITION.
# The process of using a function is known as "calling a function" or "invoking a function"

# Sometimes you don't need to know the function body, that is, what a function does internally.
# This is actually the main advantage of using functions: CODE ABSTRACTION.
# Let's take as an example the function sqrt(x), that computes the square root of a number x. 
# Do you really care how the square root is computed? When you need the square root of a number you just type
# y = sqrt(x)
# And you are done! You do not need to know how the function is doing that!
# In this case, all you need to know is the function signature, that is
# The function name (sqrt in this case)
# The function inputs (x is a float number in this case)
# The function outputs (y is a float number in this case)
# Even simpler example of this are the functions 
# print(x)
# x = input("message")
# That you have used until now.

# When exploring the documentation of new package, you will often find the signature of each function
# explained in detail. This is also known as Application Programming Interface or API.

# Another quality of functions is CODE REUSABILITY.
# Let's say you write 300 lines of code to solve a problem 
# If you ENCAPSULATE your problem in a function, you don't have to write that code ever again.
# Looking at the previous example of sqrt(x), you can think that a programmer
# wrote a very complex routine to compute the square root of a number, and you can use it every
# time you want without having to write it again.

# Functions in python are defined using the keyword def
'''def function_name(input1, input2, etc):
    #function body here
    return output
'''
# Like ifs, after the function signature you have to start a new code block using indentation.
# Functions in python can have multiple inputs but just 1 output.
# The return keyword is used to specify the return argument, and in general
# to exit from the function call.

# Here are some examples of functions:
# Sum takes two numbers and returns their sum
def sum(a, b):
    return a + b

number1 = 3
number2 = 5

print("The sum of", number1, "and", number2, "is", sum(number1, number2))

# maximum takes two numbers and returns their maximum
def maximum(a, b):
    if a >= b:
        return a
    return b

number3 = 7
number4 = 8
print("The maximum between", number3, "and", number4, "is", maximum(number3, number4))

# isEven takes one number and returns True if the number is even, False otherwise
def is_even(a):
    return a % 2 == 0

number5 = 5
if(is_even(number5)):
    print(number5, "is an even number")
else:
    print(number5, "is an odd number")

# Functions arguments in python are positional. Take this example:
def compute_stuff(a, b):
    return a / b + 5
# This function will return different outputs based on how it is called, for example
print("computeStuff(5, 3)", compute_stuff(5, 3)) 
print("computeStuff(3, 5)", compute_stuff(3, 5))

# Python gives a way around argument positionality by specifing the argument names when calling the function
# For example
print("computeStuff(a = 5, b = 3)", compute_stuff(a = 5, b = 3)) # yields the same result as 
print("computeStuff(b = 3, a = 5)", compute_stuff(b = 3, a = 5))

# Sometimes you can find/define functions with pre-defined arguments
def greet(name, msg="Good morning!"):
    print(name, ",", msg)

greet("Marco")
greet("Marco", "How are you?")

# As final tips: 
# Unless you have a very good reason to do so, do not use print() or input() inside of a function.
# Get used to think about your code divided in functions. This will make your code easily reusable in the future