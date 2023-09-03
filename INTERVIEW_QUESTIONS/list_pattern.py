# Define the initial list
lst = [10, 8, 6, 4, 2]

# Loop through the range of the length of lst and print out the slice of the list
for i in range(len(lst)):
    print(*lst[:len(lst)-i])

# Output:
# 10 8 6 4 2
# 10 8 6 4
# 10 8 6
# 10 8
# 10


l=[map(sorted(lst),lst)]
# print(l)
for d in range(len(lst)):
    print(lst[:len(lst)-d])