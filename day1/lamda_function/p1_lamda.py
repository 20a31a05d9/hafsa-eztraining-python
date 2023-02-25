# even no teeskoni list lo sqrt chyali by using lambda
l=[]
for i in range(1,15):
    if i%2==0:
      #print(i)
      l.append(i) 
print(l)    #l=[2,4,6,8,10,12,14] 
     
import math
res=map(lambda n:math.sqrt(n),l)   # n place lo direct ga l kuda pettochu
print(list(res))