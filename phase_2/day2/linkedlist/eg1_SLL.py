# creating node declaration and defination 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:               # single linked list
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp = self.head # temp+first node 
            while temp:
                print (temp.data,"-> ",end='') # temp.data means 1st nodes data
                temp=temp.next # establishing link

obj=sll()  # object creation of class sll

# node creation - initializing 
n=Node('w')  # so n.data in Node class will be w
obj.head=n  # assigning 1st node as head 
n1=Node('i') 
obj.head.next=n1   # next node value 
n2=Node('n')
n1.next=n2
n3=Node('n')
n2.next=n3
n4=Node('e')
n3.next=n4
n5=Node('r')
n4.next=n5  

obj.display()


#w -> i -> n -> n -> e -> r -> 
# r pakkana null 

            