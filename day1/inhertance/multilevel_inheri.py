# 1 parent and one child

class grandparent:  #base class 1
    def gdisplay(self):
        print('grandparent class')

class parent(grandparent):   #base class 2  (grandparent)
    def pdisplay(self):
        print('parent class')

# derived/child class
class child(parent):          #(parent)
    def cdisplay(self):
        print('child class')

obj=child()  #obj name=class name
obj.gdisplay()
obj.pdisplay()
obj.cdisplay()
