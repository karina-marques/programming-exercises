# There are two python statements that can be used only in the context of loops (both for and while)
# These statements are continue and break

# The break statement, breaks out of the innermost enclosing for or while loop.
# The continue statement, continues with the next iteration of the loop.

# Let's see an example of continue:

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
    continue
print("Found an odd number", num)

# Loop statements may have an else clause; 
# it is executed when the loop terminates through exhaustion of the iterable (with for)
# or when the condition becomes false (with while), 
# but not when the loop is terminated by a break statement. 

# Example of this

def loop_break_if_list_contains_three(input_list):
    for element in input_list:
        if(element == 3):
            print("Breaking the loop")
            break
        print(element)
    else: # This is executed only if the loop does not break
        print("Finished the loop without breaks")

loop_break_if_list_contains_three([4,"marco",5])
loop_break_if_list_contains_three([4,3,"marco"])
