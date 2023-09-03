
class Pycharm:
    def execute(self):
        print("Can type code ")
        print("Can run code ")

class Vscode:
    def execute(self):
        print("can debug")
        print("can execute")

class Laptop:
    def code(self,ide):
        ide.execute()

# ide=Pycharm()
ide=Vscode()
obj=Laptop()
obj.code(ide)

mylist=[1,0,1,0,1,0,1,0,1]
print(mylist.sort(reverse=True))
print(mylist)