def check_prime(number):
    flag=0
    if number==1:
        print("Not a prime number")
    else:
        print("checkimmmmmmmmmmmmmmm")
        for x in range(2,number):
            print(x,number)
            if number%x==0:
                print("Verified not a prime  number")
                flag=1
    if flag==0:
        print("Its a prime number")
            
check_prime(2)
# print(len(range(2,3)))