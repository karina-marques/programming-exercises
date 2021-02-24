# Loops are a construct present in every programming language
# to repeat a block of code multiple times.
# The most basic form of loop in python is the while loop, with the following syntax
''' 
while condition:
    code block
'''
# This works exactly as an if, with the difference that after the code block is finished
# the condition is evaluated again. Execute this script to see the differenct

print("If x > 0:")
x = 5
if x > 0:
    print(x)
    x -= 1

print("while x > 0:")
while x > 0:
    print(x)
    x -= 1 

# Loops are often used in conjunction with integer variables called counters
# These are variables used to count the number of iterations
# For example, let's say that we want to execute a code block 5 times, we
# can do this like this

counter = 0 # initializing the counter
while counter < 5: # We want to execute the code block 5 times
    print("Iteration number", counter)
    counter += 1