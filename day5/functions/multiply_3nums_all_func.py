'''
#1 without args and without return values

def multi():
    n1=int(input("enter number"))   #user input
    n2=int(input("enter number"))
    n3=int(input("enter number"))
    prod=n1*n2*n3
    print(prod)
multi()

#2 without args and with return values

def multi():
    n1=int(input("enter number"))   #user input
    n2=int(input("enter number"))
    n3=int(input("enter number"))
    prod=n1*n2*n3
    return prod    #print(prod)

res=multi()    # store this(return) in a variable 
print(res)   #now print it


'''

'''
#3 with args and without return values
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

'''

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
