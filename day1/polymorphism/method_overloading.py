class moverload:
    def display (self,a=None ,b=None):
        print(a,b)

obj=moverload()
print("without arguments")
obj.display()

print("with all arguments")
obj.display(20,70)

print("with one argument")
obj.display(10)
