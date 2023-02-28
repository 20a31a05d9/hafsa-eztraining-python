class a:
    n=30
class b(a):
    def calc(self):
        c=self.n+70   #dot 
        print(c)

obj =b()
obj.calc()