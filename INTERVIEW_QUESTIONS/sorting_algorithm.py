data_set=["4","2","6","1"]
def find_square(k):
    print("test...")
    k=k*2
    return k
l=[int(i) for i in data_set]
out=l.sort(key=find_square)
print(out)

