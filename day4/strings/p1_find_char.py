s,ch = input("enter a string:"),input('enter a character :')

'''
#1
if ch in s:
    print("yes")
else:
    print("no")

'''

'''
#2
for i in s:
    if i==ch:
        flag=1   #flag =0,1,0,1,0,1,0,1 ala ipoddi break chyakapote unna lydu anystadi last lo lykapote
        break        #break continue flag ---jump statements     
    else:
        flag=0

if flag==1:
    print(" there")
else:
    print("there")

'''
#3
a= "yes" if ch in s else "no"
print(a)

