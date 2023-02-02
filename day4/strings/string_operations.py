s='Hi i"m hafsa'   
print(s)

s='Hi i"m hafsa'  
s1='Hi i"m hafsa'  
#concat
print(s+s1)
#repeat
print(s*3)

#upper
print(s.upper())
#print(s)

#lower
print(s.lower())  # or 
print(s.casefold())

#capitalise      ----only 1st letter of sentence
print(s.capitalize())

#
print(s.replace('h','a'))

#
s='   Hi i"m   hafsa   '     #1st last spaces ye teestaadi ante
print(s.strip())
#print(s)

#
s='Hi i"m hafsa'
print(s.split()) #split() annadi aa string lo aa letter ekkada undo akkada split avtadi , ekkada space
print(s.split('i'))      
print(s.split('h'))       #case sensitive   
#print(s.split('.'))   # string lo dot lydu kabatti avvadu

#center
print(s.center(22,'$'))      #31 length lo majjulo istadi string     #(width,fillchar))

#count
s='Hi fff i"m fff hafsa'
print(s.count('a'))
print(s.count('f',0,len(s)))    #index 0 
print(s.count('f',8,len(s)))     #from index 8

#