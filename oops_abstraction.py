"""For example, people do not think of a car as a set of thousands of individual parts. 
Instead they see it as a well-defined object with its own unique behavior. 
This abstraction allows people to use a car to drive without knowing the complexity of the parts that form the car.
They can ignore the details of how the engine transmission, 
and braking systems work. Instead, they are free to utilize the object as a whole."""

"""Abstract Classes and Methods in Python
To declare an Abstract class, we firstly need to import the abc module. Let us look at an example."""

from abc import ABC,abstractmethod
class abs_class(ABC):
     #abstract methods
     pass

#Here, abs_class is the abstract class inside which abstract methods or any other sort of methods can be defined.

# As a property, abstract classes can have any number of abstract methods coexisting with any number of other methods.
# For example we can see below.

from abc import ABC, abstractmethod
class abs_class(ABC):
    #normal method
    def method(self):
        #method definition
        pass
    @abstractmethod
    def Abs_method(self):
        #Abs_method definition
        pass

# Here, method() is normal method whereas Abs_method() 
# is an abstract method implementing @abstractmethod from the abc module.

class Absclass(ABC):
    def printdata(self,x):
        print("received value:{}".format(x))
    @abstractmethod
    def task(self):
        print("we are inside abstract method") 
 
class TestClass(Absclass):
    def task1(self):
        print("We are inside test_class task")
 
class ExampleClass(Absclass):
    def task2(self):
        print("We are inside example_class task")

#create test_class object
tobj=TestClass()
tobj.task()

#create test_class object
eobj=ExampleClass()
eobj.task()