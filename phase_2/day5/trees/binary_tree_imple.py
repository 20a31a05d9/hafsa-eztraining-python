class binarytreenode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

node1=binarytreenode(50)
node2=binarytreenode(20)
node3=binarytreenode(45)
node4=binarytreenode(11)
node5=binarytreenode(15)
node6=binarytreenode(30)
node7=binarytreenode(78)

node1.leftchild = node2
node1.rightchild = node3

node2.leftchild = node4
node2.rightchild = node5

node3.leftchild = node6
node3.rightchild = node7


#print("root node")
print(node1.data)

#print("leftchild of the node")
print(node1.leftchild.data)

#print("rightchild of the node")
print(node1.rightchild.data)

#print("node2 is")
print(node2.data)

#print("leftchild of the node")
print(node2.leftchild.data)

#print("rightchild of the node")
print(node2.rightchild.data)


#print("root node")
print(node3.data)

#print("leftchild of the node")
print(node3.leftchild.data)

#print("rightchild of the node")
print(node3.rightchild.data)

'''

#print("node2 is")
print(node4.data)

#print("leftchild of the node")
print(node4.leftchild.data)

#print("rightchild of the node")
print(node4.rightchild.data)

'''