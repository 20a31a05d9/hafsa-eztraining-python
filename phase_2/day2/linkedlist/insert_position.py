class node:   #creating
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:   #traverse 
    def __init__(self):
        self.head=None

#-----------------------------------------
    def insert_position(self,pos,data): # hereeeeeeeeeeeeee
       np=node(data)
       temp=self.head
       for i in range(pos-1):   #pos-1-1 coz range gives -1
          temp=temp.next
       #np.data=data
       np.next=temp.next
       temp.next=np
#-------------------------------------------

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp:
             print(temp.data,'-> ',end='')
             temp=temp.next

obj=sll()

n=node(10)
obj.head=n
n1=node(20)
n.next=n1
n2=node(30)
n1.next=n2
n3=node(40)
n2.next=n3
n4=node(50)
n3.next=n4

print("before inserting 999")
obj.display()

print('')

print("after inserting 999")
obj.insert_position(2,999)
obj.display()

print('')
'''
print("after inserting 555")
obj.insert_beginning(555)
obj.display()
'''