#the string representation of an object WITH the __str__() function:

class Person():
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name

obj=Person("vipin") #or just Person
print(obj.name)
print(obj)