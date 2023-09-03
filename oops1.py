# The _init_ method is run as soon as an object of a class is created. 
# This method is useful for passing initial value to your objects. 

class employee():
    def __init__(self,age,name,id,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.id=id
obj=employee(12,"vipin",1,20000)
print(obj.name)


