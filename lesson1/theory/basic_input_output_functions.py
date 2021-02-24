# You can use the function print() print the value of anything on screen, for example

x = 5
print(x)

# Print accepts multiple arguments, that will be concatenated when flushing them out on the screen

print("The value of x is", x)

# You can use the function input() to request a value from the user on the console

x = input("Please insert the value of x: ")
print("The value of x is", x)

# Input can be used in combination with the int(), float() and str() functions to make sure that
# what is inserted is of a certain type, for example

x = int(input("Please insert the value of x: "))

# In the above example we are sure that x is an integer
# If we try to input a string we get an error
# If we try to input a floating point number (like 5.4) it gets truncated (to 5 in this case)
# The work performed by the functions int(), float() and str() is called CASTING
# Other possible example of input casting

x = str(input("Please insert a string:"))
x = float(input("Please insert a floating point number:"))
