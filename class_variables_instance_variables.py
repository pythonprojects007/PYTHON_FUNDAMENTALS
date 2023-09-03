class Car:
    wheels=4
    def __init__(self):
        self.milage=10 #instance variable
        self.company="BMW"

obj1=Car()
obj2=Car()
Car.wheels=5
print(obj1.milage,obj1.company,obj1.wheels)



