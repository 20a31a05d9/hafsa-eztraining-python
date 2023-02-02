'''
#1
n=10.9
print(type(n))

'''
''' 
#2
n=10
result =n-int(n)
if (result ==0 or result <0 ):     # ekkada or  condition pettakapoyina parledu leyda 
    print("integer")               #r!=0 or r>0  also works but if lo float else lo int vastadi 
else:
     print("floating point")

'''
#'''
#3
n=1.55
if n==int(n):          # 1==1
    print("integer")   #1 != 1.0
elif n==float(n):       #else:
    print("floating point")    # or simply else ---float no need of elif 

#'''

'''
#3-1
n=12
if type(n)==int:         
    print("integer")   
elif type(n)==float:       
    print("floating point")

'''
'''
#4
n=2.77
if isinstance(n,int)==True:
    print("integer")               
else:
     print("floating point")

'''
'''
#5
n=1.0
if n%1==0:                   # 1.0 ,2.0 iste kuda int aneystundi not good
    print("integer")          #doesnt work  ,waste    
else:
     print("floating point")
'''

