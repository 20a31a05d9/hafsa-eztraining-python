import datetime as d

a=d.datetime.now()
print(a)

x=a.strftime("%Y")   #upper case
y=a.strftime("%y")    #lower case
print("year short version ",x)
print("year full version ",y)

#x=a.strftime("%M")   #upper case
y=a.strftime("%m")    #lower case
#print("month short version ",x)
print("month full version ",y)
