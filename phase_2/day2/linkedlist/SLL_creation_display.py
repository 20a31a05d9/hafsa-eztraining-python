# creating node declaration and defination 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class sll:               # creating single linked list with no elements
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
n=Node(10)  # so n.data in Node class will be 10
obj.head=n  # assigning 1st node as head 
n1=Node(20) 
obj.head.next=n1   # next node value 
n2=Node(30)
n1.next=n2
obj.display()


#10 -> 20 -> 30 -> 
#30 pakkana null
            