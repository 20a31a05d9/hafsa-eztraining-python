'''
size=int(input("enter size of list:"))
l=[]
sum=0 
prod=1
for i in range(size):
    ele=int(input("enter element"))
    l.append(ele)
print("the list is",l)

#b=l    if we want we can take the list in a new variable ----check once think didnt work 

for j in l:
    sum =sum+j
    prod=prod*j
print("the sum is:",sum)
print("the prod is",prod)
if prod<750:
    print(prod)
elif prod>=750:    #else:
    print(sum)


'''
#simplified

n=list(map(int,input("enter elements").split())) 
print(n)

s=0
p=1
for i in n:
    s=s+i
    p=p+i
if s<=750:
    print("product",p)
else:
    print("sum",s)






