# The super() function is used to give access to methods and properties of a parent or sibling class.

# The super() function returns an object that represents the parent class.

class Car():
    def __init__(self,text):
        self.text=text

    def message(self):
        print(self.text)
        
class ChildCar(Car):
    def __init__(self,text):
        super().__init__(text)  #to initialize parent class init function ie constructor

obj=ChildCar("my super class")

obj.message()
