
class Dog:

    """ A simple class example """
    
    kind = 'canine'  # class variable shared by all instances

    def __init__(self, name):
        # The Dog class creates objects with instances customized to a specific initial state
        self.name = name    # instance variable unique to each instance
        self.tricks = []
        
    def add_trick(self, trick):
        self.tricks.append(trick)

class Warehouse:
    # The Warehouse class creates objects with instances having no specific initial state
    purpose = 'storage'
    region = 'west'

    def intro(self):
        return 'hello world'

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)
        
d = Dog('Fido')  # this creates an instance of the class Dog 
e = Dog('Buddy') # and assigns this object to the local variable d,e,f
f = Dog(2) 

print(d.kind)  # shared by all dogs
print(e.kind)  # data attributes correspond to “instance variables”
print(d.name)  # unique to d
print(e.name)  # unique to e
print(f.name)
print(e.__doc__)

print()
d.add_trick('roll over') # a method object (instance attribute reference) 
e.add_trick('play dead') # method object --- a function that “belongs to” an object
Dog.add_trick  # function oject -- this is different from method object
print(e.tricks)
print(d.tricks)

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)

print()
w1.intro() # calling a method: the instance object is passed as the first argument of the function
print(w1.intro()) # w1.intro() is equivalent to Warehouse.intro(w1)

"""
In general, calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.

Generally speaking, instance variables are for data unique to each instance and class variables are for attributes and methods shared by all instances of the class.

Often, the first argument of a method is called self. This is nothing more than a convention: the name self has absolutely no special meaning to Python. Note, however, that by not following the convention your code may be less readable to other Python programmers, and it is also conceivable that a class browser program might be written that relies upon such a convention.

Methods may call other methods by using method attributes of the self argument:
"""
