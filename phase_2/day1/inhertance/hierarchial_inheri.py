#heirarchial-- one parent and more than one child

class parent:
    def display(self):
        print('parent class')

# derived classes
class child1(parent):
    def c1show(self):
        print('child class 1')

class child2(parent):
    def c2show(self):
        print('child class 2')

# objs of c1 and c2
obj1=child1()
obj2=child2()

obj1.display()
obj1.c1show()

obj2.display()
obj2.c2show()
