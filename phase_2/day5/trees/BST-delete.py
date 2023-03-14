class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def insert(node,key):      
    # if tree is empty,return a new node
    if node is None:
        return Node(key)
    # otherwise recurse down the tree
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
        # return the (unchanged) node pointer
    return node

# entire tree need not to be searched
def minvaluenode(node): # right sub tree
    current=node
    # loop down to find the leftmost leaf
    while (current.left is not None):
        current= current.left
    return current

#given a binary search tree and a key,this function delete the key and returns the new root
 
def deleteNode(root,key):
    #base class
    if root is None:
        return root
    #if key < root,it lies in left subtree  
    if key < root.key:
        root.left = deleteNode(root.left,key)  
    elif key > root.key:
        root.right = deleteNode(root.right,key) 
        # if the key is sameas roots key then this is to be deleted
    else:
        # node with only one child or no child
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp =root.left
            root=None
            return temp
            # node with 2 children 
            #get the inorder successor (smallest in the right subtree)
            temp=minvaluenode(root.right)
            #copy the inorder successors content to this node
            root.key=temp.key
            #delete the inorder successor
            root.right=deleteNode(root.right,temp.key)
    return root

'''  BST
            50

          30   70

        20 40  60 80

        '''

root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)

print("inorder traversal of the given tree ")
inorder(root)

print('\n delete 20')
root=deleteNode(root,20)

print("inorder traversal of the modified tree ")
inorder(root)

print('\n delete 30')
root=deleteNode(root,30)

print("inorder traversal of the modified tree ")
inorder(root)

print('\n delete 50')
root=deleteNode(root,50)

print("inorder traversal of the modified tree ")
inorder(root)
