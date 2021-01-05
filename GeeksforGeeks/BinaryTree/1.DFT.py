class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end=" ")
        inOrder(root.right)

def preOrder (root):
    if root:
        print(root.data,end=" ")
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=" ")

if __name__=="__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("InOrder: ")
    inOrder(root)
    print()

    print("PreOrder: ")
    preOrder(root)
    print()

    print("PostOrder: ")
    postOrder(root)
    print()


# TC = O(n)
# SC = O(n)
