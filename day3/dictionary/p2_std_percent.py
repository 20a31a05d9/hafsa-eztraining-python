'''
l1=["a",'b','c']
l2=[100,200,300]
total=500
for i in l2:
    percent = i/ total * 100
    print(percent)
    #l3=list[percent]
    i=i+1
    l3=[percent]
print(l3)
d={a:b for j in l2 }
print(d)

'''

import random
std_names=list(map(str,input("enter names: ").split()))
marks=[]
for i in range(len(std_names)):
    a=(random.randint(100,500)/500)*100
    marks.append(a)

my_dict={x:y for (x,y) in zip(std_names,marks)}
print(my_dict)

