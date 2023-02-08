class employee:
    def __init__(self,name,id):  #init is constructor ,gives life to the object 
        self.id=id
        self.name=name
    def display(self):
        print("ID: %d \nNAME: %s" % (self.id,self.name))

emp1=employee("john",101)
emp2=employee("david",102)

emp1.display()
emp2.display()


