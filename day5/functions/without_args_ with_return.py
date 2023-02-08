#2 without args and with return values

def multi():
    n1=int(input("enter number"))   #user input
    n2=int(input("enter number"))
    n3=int(input("enter number"))
    prod=n1*n2*n3
    return prod    #print(prod)

res=multi()    # store this(return) in a variable 
print(res)   #now print it