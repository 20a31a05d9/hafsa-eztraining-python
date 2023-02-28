# abstract to concrete

from abc import ABC,abstractmethod 
class abstractdemo(ABC):
    @abstractmethod  #makes the methid abstract from @absmeth #1st absmeth 
    def display(self):
        None     # any code undachu none kakunda not syntax
    @abstractmethod   # 2nd absmeth 
    def show(self):
        None 

#changing abstract to concrete 

class demo(abstractdemo):
    def display(self):
        print("abstraction method")
    def show(self):
     print("2nd function")

obj=demo()  # object creation
obj.display()
obj.show()
