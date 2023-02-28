# one parent and one child

class parent:
    def display(self):
        print('parent class')

# derived class
class child(parent):
    def show(self):
        print('child class')

obj=child()
obj.display()
obj.show()

'''

parent
^
|
|
child

'''