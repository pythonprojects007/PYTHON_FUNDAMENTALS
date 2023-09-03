#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

class Person():
    def __init__(self,fname,lname):
        print("started...........")
        self.first_name=fname
        self.last_name=lname

    def print_names(self):
        print(self.first_name,self.last_name)

obj1=Person("vipin","Mathew")

obj1.print_names()


#Creating a child class

# To create a class that inherits the functionality from another class,
# send the parent class as a parameter when creating the child class:

class Student(Person):
    pass
obj2=Student("nidhin","k.s")
obj2.print_names()

# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
class Student(Person):
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
        
obj3=Student("alex","m")
obj3.print_names()# will throw error TypeError: Student.__init__() missing 1 required positional argument: 'age'
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
    def __init__(self,fname,lname,age):
        self.first_name=fname
        self.last_name=lname
        self.age=age
        Person.__init__(self,fname,lname)
obj4=Student("alex","m",45)
obj4.print_names()

# Python also has a super() function that will make the child class
# inherit all the methods and properties from its parent:

class Student(Person):
    def __init__(self,fname,lname):
        super.__init__(fname,lname)


##Multiple inheritance 
#A class can be derived from more than one superclass in Python. This is called multiple inheritance.

#https://www.programiz.com/python-programming/multiple-inheritance