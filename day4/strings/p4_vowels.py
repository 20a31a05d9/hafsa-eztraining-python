l=["a",'e','i','o','u','A','E','I','O','U']
s = input("enter a string:")
count=0
for i in s:
    if i in l:            # lyda for j in l:
        count=count+1
print(count)