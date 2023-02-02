#1

d={n:n*n for n in range(1,5)}
print(d)

#2
#calculating prod price for 5 umits
old ={'rice':60,'dhaal':40,'oil':120}
new={product:price*5 for (product,price) in old.items()}
print(new)

#3
#with checks
real={'sam':25,"jesse":16,"ramu":34}
now={name:age for (name,age) in real.items() if age>24}
print(now)

#using lists
l1=["a",'b','c']
l2=[1,2,3]
d={a:b for(a,b) in zip(l1,l2)}
print(d)