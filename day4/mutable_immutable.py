#immutable
# integer
x=20
print(x)
print(id(x))
x=x+x
print(x)
print(id(x))

#float
y=12.5555
print(y)
print(id(y))
y=y+y
print(y)
print(id(y))

#bool




#mutable
#list
l=[2,3,4]
print(l)
print(id(l))
print(l.append(7))     # no  change in address
print(l)
print(id(l))