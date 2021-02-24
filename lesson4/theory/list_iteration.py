# Lists (also known as sequences or arrays) are collection of elements
# The basic property of a list is the fact that the elements are
# stored one next to the other, and can be accessed using 
# integer indeces
# For example, let's define a list

a = [1, 5, "marco", 7] # Lists in python can contain different types

print("Element at index", 0, "of the list:", a[0])
print("Element at index", 2, "of the list:", a[2])

# This is also called array indexing.
# In order to index a list from the end instead that from the start
# We can use negative indices

print("Last element of the list:", a[-1])
print("Second to last element of the list:", a[-2])

# To obtain the number of elements in a list, we can use the
# len() function

print("The length of the list a is", len(a))

# Sometimes, we need/want to iterate through all the elements
# of a list. This can be done in multiple ways:
# Method 1: Using a while loop and len()

print("Iterating with a while")
counter = 0
while counter < len(a):
    print("Element at index", counter, "of the list:", a[counter])
    a += 1