class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left, key)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)

if __name__=="__main__":
    root = Node(50)
    insert(root,30)
    insert(root,20)
    insert(root,40)
    insert(root,70)
    insert(root,60)
    insert(root,80)

    print("inOrder Traversal: ")
    inOrder(root)


''' TC = O(h) where h is height in worst case.
         for skewed tree, TC = O(n) '''

''' Inorder traversal of BST always produces sorted output '''

''' We can construct a BST with only Preorder or Postorder or Level Order
    traversal. Note that we can always get inorder traversal by sorting
    the only given traversal. '''

''' Number of unique BSTs with n distinct keys is Catalan Number '''    
