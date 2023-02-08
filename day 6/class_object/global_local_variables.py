class computer():
    a=10    #class variable or instance variables
    b=20
    print('class variable inside class',a)

    def config(self):     #config is a function
        c=100
        print("yes")
        print("instance access:",self.b) # we need to use self. to access the class variables inside a method


hp=computer()     #object 1
print("hp",hp.a)
print(hp.a+hp.b)

dell=computer()    #object 2
print("dell",dell.a)
hp.config()