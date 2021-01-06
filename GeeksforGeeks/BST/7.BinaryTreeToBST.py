''' Given a Binary Tree, convert it to a Binary Search Tree. The conversion
must be done in such a way that keeps the original structure of Binary Tree '''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None

def storeInorder(root,a):
    if root:
        storeInorder(root.left,a)
        a.append(root.data)
        storeInorder(root.right,a)

def NumberOfNodes(root):
    if root is None:
        return 0
    return NumberOfNodes(root.left) + NumberOfNodes(root.right) + 1

def arrayToBST(arr,root):
    if root is None:
        return
    arrayToBST(arr,root.left)
    root.data = arr[0]
    arr.pop(0)
    arrayToBST(arr,root.right)

def BinaryTreeToBST(root):
    if root is None:
        return
    arr = []
    n = NumberOfNodes(root)
    storeInorder(root,arr)
    arr.sort()
    arrayToBST(arr,root)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

if __name__=="__main__":
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)

    print("Inorder of Binary Tree: ")
    inOrder(root)
    print()

    BinaryTreeToBST(root)
    print("Inorder of BST: ")
    inOrder(root)
