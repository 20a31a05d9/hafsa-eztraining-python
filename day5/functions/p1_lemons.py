l=21
def lemonscarry():
    if n>l:
        z=n-l
        print("you have",z, "lemons extra")
    elif n<l:
        z1=l-n
        print("you have",z1,"lemons less") 

n=int(input("enter the lemons you have:"))
lemonscarry()

