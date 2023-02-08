#4 with args and with return values
#--static input--already given, not from user

def multi(n1,n2,n3):   #passing arguments
    prod=n1*n2*n3
    return prod

res=multi(1,2,5)   #passing values
print(res)

#--user input---same above program
def multi(n1,n2,n3):   #passing arguments
    prod=n1*n2*n3
    return prod

n1=int(input("enter number 1:"))   
n2=int(input("enter number 2:"))
n3=int(input("enter number 3:"))

res1=multi(n1,n2,n3)
print(res1)
