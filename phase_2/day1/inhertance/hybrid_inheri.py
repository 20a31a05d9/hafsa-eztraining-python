class parent:  #p class
    def pdisplay(self):
        print("parent class")

class child1(parent):
    def c1display(self):
        print("child class 1")  

class child2(parent):
    def c2display(self):
        print("child class 2")  

class kid1(child1):
    def k1display(self):
        print("kid class 1")  

class kid2(child1):
    def k2display(self):
        print("kid class 2")  


class kidy1(child2):
    def kd1display(self):
        print("kidy class 1")  

class kidy2(child2):
    def kd2display(self):
        print("kidy class 2")  

# 4 obj creation for kids of child1 and kidys of child2
obj1=kid1()
obj2=kid2()
obj3=kidy1()
obj4=kidy2()

#kid1,child1,parent
obj1.pdisplay()
obj1.c1display()
obj1.k1display()

#kid2,child1,parent
obj2.pdisplay()
obj2.c1display()
obj2.k2display()

#kidy1,child2,parent
obj3.pdisplay()
obj3.c2display()
obj3.kd1display()

#kidy2,child2,parent
obj4.pdisplay()
obj4.c2display()
obj4.kd2display()










'''
obj1=child1()
obj2=child2()
obj3=kid1()
obj4=kid2()

obj1.pdisplay()
obj1.c1display()
obj1.k1display()
obj1.kd1display()

obj2.pdisplay()
obj2.c2display()
obj2.k2display()
obj2.kd2display()

'''