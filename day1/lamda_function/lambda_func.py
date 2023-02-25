#anonymous function

l=[1,2,3]
r=map(lambda x:x+x,l)   #map annadi l lo unna inputs teeskoni istaadi okati okati ala
print(list(r))          #map helps to create iteration ,it returns map 

res=map(lambda n: pow(n,2),l)   #lambda --:-- syntax
print(list(res))           # l:pow(l,2)

name='hafsa'
(lambda name:print(name)) (name)