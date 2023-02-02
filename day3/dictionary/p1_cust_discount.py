
'''
name=["hafsa","sadiya","harshita","manasa","a","b","c","d"]
#print({}.fromkeys(name))
import random
discount=random.randint(1,100)
d ={name:discount for(name,discount) }
print(d)

'''

import random
cust=["hafsa","sadiya","harshita","manasa"]
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)

