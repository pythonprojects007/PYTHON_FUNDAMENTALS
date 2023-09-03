""" Write a one-liner that will count the number of capital letters in a file. 
Your code should work even if the file is too big to fit in memory."""

with open("test.txt","r") as data:
    myfile=data.read()
    count=0
    for character in myfile:
        if character.isupper():
            count=count+1
    print(count)

#count sum(1 for line in fh for character in line if character.isupper())