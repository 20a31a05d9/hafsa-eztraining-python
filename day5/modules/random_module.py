import random as r
x="i love sweets"
print(r.sample(x,4))    #gives randomly 4 chars from string

a=[1,2,3,4,5,6]         # everytime diff o/p
r.shuffle(a)
print(a)

print(r.choice(a))    #the list is now shuffled one
print(a)
b="welcome back"         #gives randomly 1 char
print(r.choice(b))    

a=r.random()             #gives randomly 1 number from 0.0 to 1.1 excluded
print(a)              

print(r.randint(1,33))        # gives a random number in integer
print(r.randrange(1,5))     

a=[10,20,30,40,50]
print(r.choices(a,k=10))    #k enni ite anni istadi A lo nundi   --only use k 
s="hello haii "
print(r.choices(s,k=14))

print(r.uniform(5,10)) # gives a random number in float,between the range and also including the range  

z=dir(r)      #dir to know all the available methods in the module
print(z)      #r --random module   ,,, as in import random as r 

