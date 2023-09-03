# x=0 
try:
    print(x)
except:
    print("error occured")
else:
    print("no error")

try:
    print(y)
except NameError:
    print("Name error occured")
except:
    print("Something else occured")
else:
    print("no error........")