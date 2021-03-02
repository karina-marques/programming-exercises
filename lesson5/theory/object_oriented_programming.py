# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

#A Class is like an object constructor, or a "blueprint" for creating objects.

#Create a Class
#To create a class, use the keyword class:

class MyClass:
    x = 5

p1 = MyClass()
print(p1.x)

# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# Modify Object Properties
# You can modify properties on objects like this:

p1.age = 40