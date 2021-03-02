# Duck typing is one of Python exclusive's feature
# It allows generic programming in the simplest of form.
# It is based on the following principle:
# If it quacks, it must be a duck


# Let's take the following example to be more concrete

def make_sound(animal):
    animal.emit_sound()
    
class Duck:
    def emit_sound(self):
        print("Quack!")
    
    def __init__(self):
        super().__init__()

class Cat:
    def emit_sound(self):
        print("Miao!")
    
    def __init__(self):
        super().__init__()

class Dog:
    def emit_sound(self):
        print("Wof!")

    def __init__(self):
        super().__init__()

# Any object of the three classes can be passed as argument to the function
# make_sound. This is because all the classes implement the method emit_sound

dog = Dog()
cat = Cat()
duck = Duck()

make_sound(dog)
make_sound(cat)
make_sound(duck)