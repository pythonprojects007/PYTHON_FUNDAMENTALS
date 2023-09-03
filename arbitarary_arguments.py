# *args

# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def countries(*name):
    print(name)
    print("My favourite country is "+name[1])

countries("Pakistan","iNDIA","bHUTAN")