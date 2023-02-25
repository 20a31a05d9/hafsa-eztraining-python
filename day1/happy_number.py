''''
def happy(n):  # method 
    for i in n:
      a=int(n)%10
      b=int(n)//10
      c = (a**2) + (b**2) 
    #print(c)
    
    if c==1:
        print("happy number")
    #else:
    elif c!=1: #c!=0 and c!=1:
        x=happy(str(c))
        print("not happy")
      
n=input("enter number:")     
res=happy(n)


'''

# 4,16,37,58,89,145

def happy(n):
  s=r=0
  while(n>=0):
    for i in range(0,len(str(n))+1):
      r=n%10
      s=s+r**2
      n=n//10
    return s

n=int(input("enter number:"))
res=n
while(res!=1 and res!=4):
  res=happy(res)
if res==1:
  print("happy number")
else:
   print("not a happy number")

