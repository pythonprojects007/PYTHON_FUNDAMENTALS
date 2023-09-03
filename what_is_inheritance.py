# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

class Person:
    def __init__(self,name):
        self.person_name =name
    def greetings(self):
        print("hello "+self.person_name)
obj=Person("vipin")
obj.greetings()

class Student(Person):
    pass
obj2=Student("vipin")
obj2.greetings()