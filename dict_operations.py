#dict creation
d={1: "hafsa",2:"s",3:"likki", 4:5.56888, 5:78}
print(d)
print(type(d))

print(d.keys())

print(d.values())
#or 
print(d[4])

print(d.items())

print(d[1])
#or 
print(d.get(1))

d.update({6:"bikki",7:66.9})
print(d)

d.pop(1)
print(d)

d.popitem()
print(d)

d.setdefault(9,"haiii")     # or just 9 ie key ---value is optional
print(d)
d.setdefault(10)   
print(d)

# to create dictionary from iterable --list tuple range
#d.fromkeys[iterable,value]   #iterable ante list tuple range  &  value annadi optional

l=["hafsa","sadiya","harshita"]
print(d.fromkeys(l))
print(d.fromkeys(l,44))

'''
z=0
for i in range(6):
 print(d.fromkeys(l,i))

'''