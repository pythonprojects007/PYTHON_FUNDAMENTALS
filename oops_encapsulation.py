"""Python Encapsulation
Encapsulation is one of the key features of object-oriented programming. 
Encapsulation refers to the bundling of attributes and methods inside a single class.
It prevents outer classes from accessing and changing attributes and methods of a class.
This also helps to achieve data hiding."""

# In Python, we denote private attributes using underscore as the prefix 
# i.e single _ or double __. For example,

class Computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("The selling price: {}".format(self.__maxprice))
    def setter(self,new_price):
        self.__maxprice=new_price

obj=Computer()
obj.sell()

#Try changing the price
obj.__maxprice=100
obj.sell() #cant change the price

# after adding setter function

obj.setter(2000)
obj.sell()