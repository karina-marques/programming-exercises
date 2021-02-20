# The syntax of the if statement is the following
# if condition:
#   code block
# It is very important to indent the code to specify the code block
# that is, whatever you want to be executed only when the condition of the 
# if is true.
# Code indentation is done automatically by Visual Code, but in case you have
# to do it manually for whetever reason, you can use Tab (the key above the caps lock)
# for right indent and shift-tab for left indent

# Below are some examples of if conditions

x = int(input("Input a number: "))

if x < 18:
    print("You cannot vote for italian parlament")
elif x >= 18 and x < 25:
    print("You can vote for \"camera dei deputati\" of the italian parlament")
else:
    print("You can vote for both \"camera dei deputati\" and \"senato della repubblica\" of the italian parlament")

print("Your age is", str(x))