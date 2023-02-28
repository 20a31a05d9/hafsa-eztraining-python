#private 
class encap:
    __a=10
    print(__a)
    def encapsulation (self):
        _b=200
        print("encap function")
        print(self.__a)

obj=encap()
#print(obj.__a)
obj.encapsulation()
print(obj.__a)  # will throw error coz a is private ,cant be accessed outside class 