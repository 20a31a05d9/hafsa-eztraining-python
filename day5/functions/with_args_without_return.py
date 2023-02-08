''' 3 with args and without return values '''
#--static input--already given, not from user

def multi(n1,n2,n3):   #passing arguments
    prod=n1*n2*n3
    print(prod)

multi(3,4,5)   #passing values

#--user input---same above program
def multi(n1,n2,n3):   #passing arguments
    prod=n1*n2*n3
    print(prod)

n1=int(input("enter number 1:"))   
n2=int(input("enter number 2:"))
n3=int(input("enter number 3:"))

multi(n1,n2,n3)