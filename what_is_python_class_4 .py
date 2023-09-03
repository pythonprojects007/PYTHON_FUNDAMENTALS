# modify_properties_on_objects

class Greetings():
    def __init__(self,message):
        self.message=message
        print("hai you can greet someone with this")
   
    def greet(self,name):
        print(self.message+name)

obj=Greetings("helloooooo    ")
obj.greet("Vipin")
obj.message="haiiiiiiiiiiiiii"
obj.greet("Vipin")
del obj.message
obj.greet("Vipin")# will throw error