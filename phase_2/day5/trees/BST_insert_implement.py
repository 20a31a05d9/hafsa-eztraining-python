#bst insert

class node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None

# a new node with the given key

def insert(root,key):
    if root is None:
        return node(key)
    else:
        if root.val==key:
            return root
        elif root.val < key:
            root.right =insert(root.right,key)
        else:
            root.left =insert(root.left,key)
    return root

#inorder traversal 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

'''
     50
  |      |
 30       70
 |  |    |   |
20  40  60   80

'''

r=node(50)
r=insert(r,30)
r=insert(r,20)
r=insert(r,40)
r=insert(r,70)
r=insert(r,60)
r=insert(r,80)
inorder(r)