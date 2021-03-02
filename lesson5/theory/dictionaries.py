# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered, changeable and does not allow duplicates.
# Dictionaries are written with curly {} brackets, and have keys and values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964, 
}
thisdict['year'] = 2020
print(thisdict['year'])


# Dictionary Length
# To determine how many items a dictionary has, use the len() function:

print(len(thisdict))
# Dictionary Items - Data Types
# The values in dictionary items can be of any data type
# The keys in dictionary are strings.

# Python Collections
# There are four collection data types in the Python programming language:

# A List [] is a collection which is ordered and changeable. Allows duplicate members. It is indexed using integer numbers
# Tuple () is a collection which is ordered and unchangeable. Allows duplicate members. It is indexed using integer numbers
# Dictionary {} is a collection which is unordered and changeable. No duplicate members. It is indexed using the key type (i.e. strings)
# Set is a collection which is unordered and unindexed. No duplicate members. It is like a dictionary with no values, just keys.
