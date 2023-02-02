
#'''

#1                    
n=[elements for elements in "great afternoon"]         #  n is a list
print(n)    

#'''
'''
#2
l=['hyd','vizag','chennai','vijayawada']
city=[]
for n in l:
    if 'v' in n:         # aa word lo v unte appudu print chystadi
      city.append(n)        # append bracket lopaldi append avtaadi
print(city)

'''
'''

#3
l1=[2**x for x in range(2,10)]
print(l1)

l2=[A for A in range(100,201,20)]
print(l2)

l3=[1,2,3,4,5,6]
l4=[i for i in l3 if (i<5)]
print(l4)

'''