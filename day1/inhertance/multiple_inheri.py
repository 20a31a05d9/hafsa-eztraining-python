# 2 parents and one child

class mom:  #parent class 1
    def mdisplay(self):
        print('mom class')

class dad:   #parent class 2
    def ddisplay(self):
        print('dad class')

# derived/child class
class child(mom,dad):
    def cdisplay(self):
        print('child class')

obj=child()
obj.mdisplay()
obj.ddisplay()
obj.cdisplay()
