class Student:
    school= "Srishti"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):#since we are passing self its an instance method(self means passing an object as an argument)
        return (self.m1+self.m2+self.m3)/3
    def set_m1(self,new_m1):
        self.m1=new_m1
    # 2 types of instance methods 
    # 1.Accessors - if we only fetch the values also called getters
    # 2.Mutators - if we modify the values also called setters
    # Now create a class method(which works with class variables )
    @classmethod  #called as decorator for class method
    def itsaclassmethod(cls):
        return cls.school
    @staticmethod
    def info():
        print("Its student class....")
obj1=Student(30,40,50)
obj1.set_m1(10)
avg=obj1.average()
print(avg)
print(Student.itsaclassmethod())
print(Student.info())
