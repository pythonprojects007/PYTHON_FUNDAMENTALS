"""Iterators in Python
Iterator in Python is an object that is used to iterate over iterable objects like lists, tuples, dicts, and sets.
The iterator object is initialized using the iter() method. It uses the next() method for iteration.

__iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
__next__(): The next method returns the next value for the iterable. When we use a for loop to traverse any 
iterable object, internally it uses the iter() method to get an iterator object, which further uses the next()
method to iterate over.
 This method raises a StopIteration to signal the end of the iteration."""

l=[1,2,3]
new_l=iter(l)
print(next(new_l))
print(next(new_l))

""" Generator-Function: A generator-function is defined like a normal function, 
but whenever it needs to generate a value, it does so with the yield keyword rather than return.
 If the body of a def contains yield, the function automatically becomes a generator function."""

def mygenerator_fun():
    yield 1
    yield 2
    yield 3

x=mygenerator_fun()
print(x)
for data in mygenerator_fun():
    print(data)

#or 

print(next(x))

print(next(x))

print(next(x))

l1=[1,2,2,4]
print(list(map(lambda x:x*x,l1)))
new_list=[]
x="hello"
print(list(map(str.lower,x)))

s="hello how are you"
s=s.split()
print(s)
print("".join([ data for data in s ]))
