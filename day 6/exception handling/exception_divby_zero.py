#try except

a=100
b=0

try: #you're telling that this may have error ,u try
    print(a/b)
#except exception: # u saying if error there i handle 
#print("cant divide any number by zero")

except Exception as e:   #except 
    print("please note ,number cant be divided any by zero",e)    #no e
    #this will print error also   

print("bye") # to see if the program executes till end or gets an error


'''
#try except finally

a=100
b=0

try:
    print("resource open")
    print(a/b)

except Exception as e:
    print("dont give 2nd num as zero",e)

finally:  # this will excetued if theres an error or not
    print("resource closed ")

    '''