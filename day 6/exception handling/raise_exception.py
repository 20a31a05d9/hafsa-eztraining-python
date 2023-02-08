x=101
if x %2!=0:    #true if x is odd ,,but we want only even numbers so raise a excep if the num is odd
    raise Exception('x shld be even number')
else:
    print("x is even number...correct")