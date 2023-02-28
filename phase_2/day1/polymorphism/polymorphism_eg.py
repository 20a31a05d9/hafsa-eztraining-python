class vizag():
    def placename(self):
        print("vizag ")
    def student(self):
        print("hafsa")    
    def year(self):
        print("3rd yr ")
class hyd():
    def placename(self):
        print("hyd ")
    def student(self):
        print("hiba")    
    def year(self):
        print("2nd yr ")

o_vizag=vizag()
o_hyd=hyd()

for details in (o_vizag,o_hyd):
    details.placename()
    details.student()
    details.year()
    


