#fuc with arg and with return 
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)        #else: pettakapoyina parledu
n=int(input("enter a number:"))
res=fact(n)
print(res)