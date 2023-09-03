#method_overloading is not possible in python
#ie add(a,b) and add(a,b,c) wont work unless it is handled in a tricky way

#Now method overrriding

class A:
    def show(self):
        x=5
        print("In A show")
class B(A):
    x=5
    def show(self):
        print(" In B show")

obj=B()
obj.show()
print(obj.x)
