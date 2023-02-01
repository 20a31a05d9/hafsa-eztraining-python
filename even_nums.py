'''l=[2,4,6,1,3,5]
for i in range(len(l)):
    if (i%2==0):             #wrong check once 
     print(l[i])

'''

size=int(input("size:"))
l=[]

for i in range(size):
    ele=int(input("enter element:"))
    l.append(ele)
print(l)

for j in range(len(l)):
    if(l[j]%2==0):
        print(l[j])

'''
membership op 
for j in l:              
    if(j%2==0):          
        print(j)           


'''
