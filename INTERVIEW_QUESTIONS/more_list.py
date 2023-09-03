
#slicing
# Lst[ Initial : End : IndexJump ]

l=[1,2,2,5]
l.pop(-1)
print(l)


print(list(range(1,10,2)))

print(list(range(1,10,3)))

dic={"vipin":"123","mathew":"456 "}

print([[index,key] for index,key in enumerate(dic)])


#list comprehension to generate even numbers

[print(data) for data in range(1,11) if data%2==0]

