#  **kwargs

# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def companies(**name):
    print(name)
    print("my favorite company is "+name["c1"])

companies(c2="apple",c3="netflix",c1="google")