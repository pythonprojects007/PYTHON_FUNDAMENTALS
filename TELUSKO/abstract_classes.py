# we cant craete object of an abstract class 

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("Checking..........   ")
class Whiteboard:
    def write(self):
        print("its writing....")
class Programmer:
    def work(self,com):
        print("Solving Bugs")
        # com.process()
# com =Computer()
w1=Whiteboard()
p1=Programmer()
p1.work(w1)
obj=Laptop()
obj.process()


    
