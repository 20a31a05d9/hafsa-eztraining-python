class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data

def printinorder(root):
    if root:
        # 1st recursion on left child
        printinorder(root.left)
        # then print the data of the node
        print(root.val,end=" ")
        # now recursion on right child
        printinorder(root.right)

def printpostorder(root):
    if root:
        # 1st recursion on left child
        printpostorder(root.left)
        # now recursion on right child
        printpostorder(root.right)
        # then print the data of the node
        print(root.val,end=" ")
        
def printpreorder(root):
    if root:
        # then print the data of the node
        print(root.val,end=" ")
        # 1st recursion on left child
        printpreorder(root.left)
        # now recursion on right child
        printpreorder(root.right)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)

print('pre-order')
printpreorder(root)
print()

print('in-order')
printinorder(root)
print()

print('post-order')
printpostorder(root)