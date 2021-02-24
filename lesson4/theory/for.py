# We have left our lesson on lists looking for other
# methods to iterate over a list. We can use the for loop.
# A for loop works like a while loop, but it is specialized
# in iterating through sequences/list.
# The syntax is the following
'''
for element in sequence:
    code block
'''
# The code block will be executed for each element in the sequence.
# The element variable will change it's content in each different iteraction of the loop
# Let's see a practical example

a = [1, 5, "marco", 7]

print("Iterating on the list with a for")
for element in a:
    print(element)

# If for some reason we want to iterate through a list indexing it in the classical way,
# that is, with integer indeces and the [] operator, we can use the range() function
# range(x) returns a list of numbers from 0 to x - 1
# for example the call range(5) returns a list like this: [0, 1, 2, 3, 4]
# range(x, y) returns a list of numbers from x to y - 1
# for example the call range(2, 5) returns a list like this: [2, 3, 4]
# More information on range here: # https://docs.python.org/3/library/stdtypes.html#range

for x in range(5):
    print(x)

# We can use range() in conjuction with len() like this

print("Iterating with a for + range(len(a))")
for counter in range(len(a)):
    print("Element at index", counter, "of the list:", a[counter])

# We can use range to execute an arbitrary code block for how many times we want