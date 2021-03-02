# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:

print("Hello")
print('Hello')

# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
# Note: in the result, the line breaks are inserted at the same position as in the code.

# Strings are Arrays!
# Square brackets can be used to access elements of the string.
# Get the character at position 1 (remember that the first character has the position 0):

a = "Hello, World!"
print(a[1])

# Unlike arrays, strings are immutable, so the index notation [] can be used only to read elements
# and not to write them. For example, the following instruction is illegal

''' a[0] = 5 '''

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
# Loop through the letters in the word "banana":

for x in "banana":
  print(x)

# String Length
# To get the length of a string, use the len() function.

a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Slicing
# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon (:), to return a part of the string.

b = "Hello, World!"
print(b[2:5])

# By leaving out the start index, the range will start at the first character:

b = "Hello, World!"
print(b[:5])

# By leaving out the end index, the range will go to the end:

b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

b = "Hello, World!"
print(b[-5:-2])