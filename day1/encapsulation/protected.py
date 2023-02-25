#protected

class encap:
    _a=10
    c=20
    def encapsulation (self):
        _b=200
        print("encap function accessing protected")
        print(self._a+11)

obj=encap()
print(obj._a)
obj.encapsulation()
print(obj.c)