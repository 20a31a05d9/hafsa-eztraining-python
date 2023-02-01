s={1,1.2,"hafsa",'h'}
print(s)
s.add(99)
print(s)
s.update([11,33,"sadiya",'s'])
print(s)
s.discard(11)
print(s)
s.remove("sadiya")        
print(s)
s.discard(44)           #lynidi iste error radu
print(s)
#s.remove("likki")        # lynidi iste error chupistadi 
#print(s)


s1={1,2,3,9}
s2={1,2,3,4,5}
print(s2.issuperset(s1))     #9 kuda unte true
print(s1.union(s2))            #s1|s2 ----union symbol
print(s1.intersection(s2))     #s1&s2 
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))     #s1^s2


