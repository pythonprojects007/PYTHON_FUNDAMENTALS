"""What is Polymorphism?
 Polymorphism is taken from the Greek words Poly (many) and morphism (forms).
It means that the same function name can be used for different types.
This makes programming more intuitive and easier."""

"""1. Polymorphism with Function and Objects"""

class Tomoto():
    def type(self):
        print("Vegetable")
    def color(self):
        print("Orange")
class Apple():
    def type(self):
        print("Fruit")
    def color(self):
        print("Red")
def myfunc(obj):
    obj.color()
    obj.type()

obj1=Tomoto()
obj2=Apple()
myfunc(obj1)
myfunc(obj2)

"""Polymorphism with Class Methods
Python uses two different class types in the same way.
Here, you have to create a for loop that iterates through a tuple of objects.
Next, you have to call the methods without being concerned about which class type each object is. 
We assume that these methods actually exist in each class.
Here is an example to show polymorphism with class:"""

class India():
    def capital(self):
        print("Delhi")
    def language(self):
        print("Hindi")
class USA():
    def capital(self):
        print("Washington")
    def language(self):
        print("English")
obj3=USA()
obj4=India()

for ob in (obj3,obj4):
    ob.capital()
    ob.language()

"""Polymorphism with Inheritance
Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class.
In inheritance, the child class inherits the methods from the parent class. 
Also, it is possible to modify a method in a child class that it has inherited from the parent class.

This is mostly used in cases where the method inherited from the parent class doesn’t fit the child class. 
This process of re-implementing a method in the child class is known as Method Overriding. 
Here is an example that shows polymorphism with inheritance:"""

class Bird():
    def intro(self):
        print("birds can fly")
    def flight(self):
        print("Most of the birds can fly but some can not")
class Parrot(Bird):
    def flight(self):
        print("Parrot can fly")
class Penguin(Bird):
    def flight(self):
        print("penguin cant fly")

obj5=Parrot()
obj5.intro()
obj5.flight()
obj6=Penguin()
obj6.intro()
obj6.flight()